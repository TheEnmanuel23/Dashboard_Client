from .models import *
from .server import Server

class configIndicators:
	def __init__(self, projectToConfig):
		self.project = projectToConfig.project
		self.cursor = projectToConfig.getCursor_Default()

	def getIndicadoresWithValueToLoadPage(self):		
		listDataOfCursor = Server.convertCursorToList(self.cursor)
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
			if indicador.id_columna in Server.getColumnsDescriptions(self.cursor):
				data.append(indicador)
		return data	

	def getRowOfCursor(self, object_id):
		rowOfCursorToReturn = None
		listDataOfCursor = Server.convertCursorToList(self.cursor)
		for cursorRow, column in ((cursorRow, column) for cursorRow in  listDataOfCursor for column in self.column_names):
			objectToFind = cursorRow[column]	
			if objectToFind == object_id:
				rowOfCursorToReturn = cursorRow
				break
		return rowOfCursorToReturn