import cx_Oracle
from .models import *

class configIndicators:
	def __init__(self, projectToConfig):
		self.project = projectToConfig.project
		self.cursor = projectToConfig.getCursor_Default()
		self.column_names = projectToConfig.getColumnsDescriptions(self.cursor)

	def getIndicadoresWithValue(self, object_id):
		data = list( )
		indicadores = self.getIndicadoresList()
		row = self.getRowOfCursor(str(object_id),)
		for indicador in indicadores:			
			data.append({
				'idIndicador': indicador.id_indicador,
				'indicador': indicador.de_indicador,
				'valor': row.get(indicador.id_columna)
			})
		return data

	def getIndicadoresList(self):
		data = list()
		allIndicadoresByProject = DxinIndicadores.objects.filter(id_proyecto = self.project.pk)
		for indicador in allIndicadoresByProject:
			if indicador.id_columna in self.column_names:
				data.append(indicador)
		return data	

	def getRowOfCursor(self, object_id):
		rowOfCursorToReturn = None
		listData = self.convertCursorToList()

		for data, column in ((data, column) for data in  listData for column in self.column_names):
			objectToFind = data[column]	
			if objectToFind == object_id:
				rowOfCursorToReturn = data
				break
		return rowOfCursorToReturn

	def convertCursorToList(self):
		dictData = list()
		for row in self.cursor:
			dictData.append(dict(zip(self.column_names, row)))
		return dictData