import cx_Oracle
from dbi_client_app.models import *
from .sql import ConfigSQL
from .where import ConfigWhereClause

class ConfigProject():
	def __init__(self, projectToConfig):
		self.project = projectToConfig
		self.connection = self.project.id_conexionbd
		self.sqlClause = ConfigSQL()
		self.whereClause = ConfigWhereClause(self.project)

	def getCursor_Default(self):
		query = self.sqlClause.settingSql(self.project.sql, self.whereClause.getQueryWithNewWhere_Default)		
		cursor = self.settingCursor(query)
		return cursor

	def getCursor_CustomizedForUser(self):
		query = self.sqlClause.settingSql(self.project.sql, self.whereClause.getQueryWithNewWhere_CustomizedForUser)
		cursor = self.settingCursor(query)
		return cursor

	def settingCursor(self, sqlToExecute_and_preconfigured):
		serverConfig = self.serverConfigurationData()		
		db = cx_Oracle.connect(serverConfig['user'], serverConfig['password'], serverConfig['tns_dsn'])
		cursor = db.cursor();
		cursor.execute(sqlToExecute_and_preconfigured)
		return cursor

	def serverConfigurationData(self):
		configurationData = {
			'ip': self.connection.nb_servidor,
			'port': self.connection.nu_puerto,
			'sid': self.connection.nb_basedatos,
			'user': self.connection.id_usuario,
			'password': self.connection.password,
			'tns_dsn': cx_Oracle.makedsn(self.connection.nb_servidor, self.connection.nu_puerto, self.connection.nb_basedatos)
		}
		return configurationData

	def getColumnsDescriptions(self, cursor):
		columns = [col[0] for col in cursor.description]
		return columns