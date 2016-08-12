import cx_Oracle
from .server import Server
from .models import *
from django.db.models import Q

class ConfigFilters:
	def __init__(self, project):
		self.project = project
		self.server = Server(self.project.id_conexionbd)

	def getFilters(self):
		filtros = DxinFiltros.objects.filter(Q(id_proyecto = self.project))
		listOfDataForeachFilter = list()
		for filtro in filtros:
			data = self.getListOfDataOfSql(filtro.sql)
			dictData = self.convertToDictionary(data)
			dictData['id_columna'] = str(filtro.id_columna)
			dictData['desc_columna'] = str('Mes')
			listOfDataForeachFilter.append(dictData)
			
		return listOfDataForeachFilter

	def getListOfDataOfSql(self, sql):
		cursor = self.server.settingCursor(sql)
		data = self.server.getDataOfCursor(cursor)
		return data

	def convertToDictionary(self, tupleOfData):
		dictOfRowSqlOfFilter = dict()
		dictOfRowSqlOfFilter['data'] = tupleOfData
		return dictOfRowSqlOfFilter
