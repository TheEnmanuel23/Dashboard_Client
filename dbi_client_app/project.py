from .server import Server
from .sql import ConfigSQL
from .where import ConfigWhereClause

class ConfigProject():
	def __init__(self, projectToConfig):
		self.project = projectToConfig
		self.server = Server(self.project.id_conexionbd)
		self.sqlClause = ConfigSQL()
		self.whereClause = ConfigWhereClause(self.project)

	def getCursor_Default(self):
		query = self.sqlClause.settingSql(self.project.sql, self.whereClause.getQueryWithNewWhere_Default)		
		cursor = self.server.settingCursor(query)
		return cursor

	def getCursor_CustomizedForUser(self):
		query = self.sqlClause.settingSql(self.project.sql, self.whereClause.getQueryWithNewWhere_CustomizedForUser)
		cursor = self.server.settingCursor(query)
		return cursor