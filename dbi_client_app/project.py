import cx_Oracle, sqlparse
from dbi_client_app.models import *
from sqlparse.sql import Where, Comparison
from sqlparse.tokens import Keyword, Whitespace

class ConfigProject():
	def __init__(self, projectToConfig):
		self.project = projectToConfig
		self.connection = self.project.id_conexionbd
		self.setCursor()

	def setCursor(self):
		sql = self.project.sql		
		self.settingWhere(sql)

		ip = self.connection.nb_servidor
		port = self.connection.nu_puerto
		sid = self.connection.nb_basedatos
		user = self.connection.id_usuario
		password = self.connection.password
		tns_dsn = cx_Oracle.makedsn(ip, port, sid)
		db = cx_Oracle.connect(user, password, tns_dsn)
		self.cursor = db.cursor();
		self.cursor.execute(sql)
		return self.cursor

	def getColumnsDescriptions(self):
		columns = [col[0] for col in self.cursor.description]
		return columns

	def settingWhere(self, sqlOriginal):
		sqlParsed = self.getSqlParsed(sqlOriginal)
		sqlAfterClauseFrom = self.extractSqlAfterClauseFrom(sqlParsed)
		queryFormated =  sqlOriginal.replace(sqlAfterClauseFrom, '')
		queryWithNewWhere = self.replaceOldWhere(queryFormated, sqlParsed)  +' ' + sqlAfterClauseFrom
		print(queryWithNewWhere)

	def replaceOldWhere(self, sql, sqlParsed):
		originalWhere = self.getWhereOfSql(sqlParsed)		
		filtros = DxinFiltros.objects.filter(id_proyecto = self.project)	
		dictWhere = self.eachFiltrosDefault(filtros, originalWhere)
		newWhere = 'where %s' % self.convertDictionaryWhereToSqlWhere(dictWhere)
		queryWithNewWhere = sql.replace(str(originalWhere), newWhere)
		return queryWithNewWhere

	def getSqlParsed(self, sql):
		return sqlparse.parse(sql)[0]

	def getWhereOfSql(self, sqlParsed):
		where = None
		for token in sqlParsed:
			if isinstance(token, Where):
				where = token
				break
		return where

	def extractSqlAfterClauseFrom(self, sqlParsed):
		sqlAfterClauseFrom = ''
		keyword_FROM_finded = False
		clause_FROM_finalized = False
		for token in sqlParsed:
			if keyword_FROM_finded:				
				if clause_FROM_finalized:					
					sqlAfterClauseFrom += token.value
				elif token.ttype is Keyword:
					sqlAfterClauseFrom += token.value
					clause_FROM_finalized = True
			elif token.ttype is Keyword and token.value.upper() == 'FROM':
				keyword_FROM_finded = True
		return sqlAfterClauseFrom

	def eachFiltrosDefault(self, filtros, portion_where):		
		dictOfWhere = self.convertClauseWhereToDictionary(portion_where)
		for filtro in filtros:
			if(filtro.in_defecto.upper() ==  'S' ):
				whereModel = WhereModel(filtro.id_columna, filtro.valor_defecto)
				self.setCondition(whereModel, dictOfWhere)
		return dictOfWhere

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