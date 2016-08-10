import cx_Oracle, sqlparse
from dbi_client_app.models import *
from sqlparse.tokens import Keyword, Whitespace
from .where import ConfigWhereClause

class ConfigProject():
	def __init__(self, projectToConfig):
		self.project = projectToConfig
		self.connection = self.project.id_conexionbd	

	def settingCursor(self, sqlToExecute_and_preconfigured):
		serverConfig = self.serverConfigurationData()
		db = cx_Oracle.connect(serverConfig['user'], serverConfig['password'], serverConfig['tns_dsn'])
		self.cursor = db.cursor();
		self.cursor.execute(sqlToExecute_and_preconfigured)
		return self.cursor

	def serverConfigurationData(self):
		configurationData = {
			'ip': self.connection.nb_servidor
			'port': self.connection.nu_puerto
			'sid': self.connection.nb_basedatos
			'user': self.connection.id_usuario
			'password': self.connection.password
			'tns_dsn': cx_Oracle.makedsn(ip, port, sid)
		}
		return configurationData

	def getSqlWithWhere_Defualt(self):
		whereClause = ConfigWhereClause(self.project)
		query = self.settingSql(self.project.sql, whereClause.getQueryWithNewWhere_Default)
		return query

	def getSqlWithWhere_CustomizedForUser(self):
		whereClause = ConfigWhereClause(self.project)
		query = self.settingSql(self.project.sql, whereClause.getQueryWithNewWhere_CustomizedForUser)
		return query

	def settingSql(self, sqlOriginal, callback_where):
		sqlParsed = self.getSqlParsed(sqlOriginal)
		sqlAfterClauseFrom = self.extractSqlAfterClauseFrom(sqlParsed)
		queryFormated =  sqlOriginal.replace(sqlAfterClauseFrom, '')
		where = callback_where(sqlOriginal, sqlParsed)
		queryWithNewWhere = "%s %s" % (where, sqlAfterClauseFrom)
		return queryWithNewWhere

	def getSqlParsed(self, sql):
		return sqlparse.parse(sql)[0]

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

	def getColumnsDescriptions(self):
		columns = [col[0] for col in self.cursor.description]
		return columns