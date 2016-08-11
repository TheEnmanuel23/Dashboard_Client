from dbi_client_app.models import *
from sqlparse.sql import Where, Comparison
from django.db.models import Q

class ConfigWhereClause:
	def __init__(self, project):
		self.project = project

	def getQueryWithNewWhere_Default(self, sql, sqlParsed):
		filtros = self.getFiltros(onlyDefault=True)
		queryWithNewWhere = self.getQueryWithNewWhere(sql, sqlParsed, filtros)
		return queryWithNewWhere

	def getQueryWithNewWhere_CustomizedForUser(self, sql, sqlParsed):
		filtros = self.getFiltros(onlyDefault=False)
		queryWithNewWhere = self.getQueryWithNewWhere(sql, sqlParsed, filtros)
		return queryWithNewWhere

	def getQueryWithNewWhere(self, sql, sqlParsed, filtros):
		originalWhere = self.getWhereOfSql(sqlParsed)
		dictWhere = self.eachFiltros(filtros, originalWhere)
		newWhere = 'where %s' % self.convertDictionaryWhereToSqlWhere(dictWhere)
		queryWithNewWhere = sql.replace(str(originalWhere), newWhere)
		return queryWithNewWhere

	def getFiltros(self, onlyDefault):
		filtros = None
		if onlyDefault:
			filtros = DxinFiltros.objects.filter(Q(id_proyecto = self.project) 
						and 
						(Q(in_defecto='S')| Q(in_defecto='s')))
		else :
			filtros = DxinFiltros.objects.filter(Q(id_proyecto = self.project)	
						and 
						(Q(in_defecto='N')| Q(in_defecto='n')))
		return filtros

	def getWhereOfSql(self, sqlParsed):
		where = None
		for token in sqlParsed:
			if isinstance(token, Where):
				where = token
				break
		return where

	def eachFiltros(self, filtros, portion_where):		
		dictOfWhere = self.convertClauseWhereToDictionary(portion_where)
		for filtro in filtros:
			whereModel = WhereModel(filtro.id_columna, filtro.valor_defecto)
			self.setCondition(whereModel, dictOfWhere)
		return dictOfWhere

	def filtros(self, filtros):
		dictOfWhere = self.convertClauseWhereToDictionary(portion_where)

	def setCondition(self,whereModel, dictionaryOfData):
		value = self.removeSingleQuotes(whereModel.column_value)
		dictionaryOfData[whereModel.column_name] = "'%s'" % (value)
		return dictionaryOfData

	def removeSingleQuotes(self, stringToRemoveSingleQuotes):
		newString = stringToRemoveSingleQuotes.replace("'", '')
		return newString

	def convertDictionaryWhereToSqlWhere(self, dictionaryOfWhere):
		conditions = ''
		i = 1
		for item in dictionaryOfWhere:
			conditions += "%s=%s" % (str(item), str(dictionaryOfWhere[item]))
			if i < len(dictionaryOfWhere):
				conditions += ' and '
			i += 1
		return conditions

	def convertClauseWhereToDictionary(self, portion_where = ''):
		conditions = dict()
		if portion_where:
			for token in portion_where:
				if isinstance(token, Comparison):
					tupleOfData = self.convertComparisionToTuple(token)
					conditions[tupleOfData[0]] = tupleOfData[-1]
		return conditions

	def convertComparisionToTuple(self, comparision):
		tupleOfData = tuple()
		for item in comparision:
			if not str(item).isspace():
				tupleOfData += (str(item),)
		return tupleOfData

class WhereModel:
	column_name = ''
	column_value = ''

	def __init__(self, column_name, column_value):
		self.column_name = column_name
		self.column_value = column_value