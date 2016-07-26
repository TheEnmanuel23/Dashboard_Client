import cx_Oracle
from dbi_client_app.models import *

class ConfigProject():
	def __init__(self, projectToConfig):
		self.project = projectToConfig
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

	def getColumnsDescriptions(self):
		columns = [col[0] for col in self.cursor.description]
		return columns