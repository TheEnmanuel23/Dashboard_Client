import cx_Oracle
from .models import *

class ConfigProject():
	def __init__(self, project):
		self.project = project
		self.connection = self.project.id_conexionbd
		self.setCursor()

	def setCursor(self):
		sql = self.project.sql
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

	def getIndicadoresList(self):
		data = list()
		allIndicadoresByProject = DxinIndicadores.objects.filter(id_proyecto = self.project.pk)
		for indicador in allIndicadoresByProject:
			if indicador.id_columna in self.getColumnsDescriptions():
				data.append(indicador)
		return data

	def getColumnsDescriptions(self):
		columns = [col[0] for col in self.cursor.description]
		return columns

	def getIndicadoresWithValue(self):
		data = list( )
		indicadores = self.getIndicadoresList()
		row = self.getRowOfCursor('PET')
		for indicador in indicadores:			
			data.append({
				'idIndicador': indicador.id_indicador,
				'indicador': indicador.de_indicador,
				'valor': row.get(indicador.id_columna)
			})
		return data

	def getRowOfCursor(self, object_id):
		rowOfCursorToReturn = None
		columns = self.getColumnsDescriptions()
		listData = self.convertCursorToList()

		for data, column in ((data, column) for data in  listData for column in columns):
			objectToFind = data[column]	
			if objectToFind == object_id:
				rowOfCursorToReturn = data
				break
		return rowOfCursorToReturn

	def convertCursorToList(self):
		dictData = list()
		columns = self.getColumnsDescriptions()
		for row in self.cursor:
			dictData.append(dict(zip(columns, row)))			
		return dictData