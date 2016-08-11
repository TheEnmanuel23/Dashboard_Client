import cx_Oracle
from .models import *

class configIndicators:
	def __init__(self, projectToConfig):
		self.project = projectToConfig.project
		self.cursor = projectToConfig.getCursor_Default()
		self.column_names = projectToConfig.getColumnsDescriptions(self.cursor)

	def getIndicadoresWithValueToLoadPage(self):		
		listDataOfCursor = self.convertCursorToList()
		data = self.getIndicadoresWithValue(listDataOfCursor[0])
		return data

	def getIndicadoresWithValueAjax(self, object_id):
		row = self.getRowOfCursor(str(object_id),)
		data = self.getIndicadoresWithValue(row)
		return data

	def getIndicadoresWithValue(self, rowIndicador):
		data = list( )
		indicadores = self.getIndicadoresList()
		for indicador in indicadores:			
			data.append({
				'idIndicador': indicador.id_indicador,
				'indicador': indicador.de_indicador,
				'valor': rowIndicador.get(indicador.id_columna)
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
		listDataOfCursor = self.convertCursorToList()
		for cursorRow, column in ((cursorRow, column) for cursorRow in  listDataOfCursor for column in self.column_names):
			objectToFind = cursorRow[column]	
			if objectToFind == object_id:
				rowOfCursorToReturn = cursorRow
				break
		return rowOfCursorToReturn

	def convertCursorToList(self):
		dictData = list()
		for row in self.cursor:
			dictData.append(dict(zip(self.column_names, row)))
		return dictData