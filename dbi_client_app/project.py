import cx_Oracle, sqlparse
from dbi_client_app.models import *
from sqlparse.tokens import Keyword, Whitespace
from .where import ConfigWhereClause

class ConfigProject():
	def __init__(self, projectToConfig):
		self.project = projectToConfig
		self.connection = self.project.id_conexionbd

	def settingCursorDefault(self):
		sql = self.project.sql
		newSql = self.settingSql(sql)
		ip = self.connection.nb_servidor
		port = self.connection.nu_puerto
		sid = self.connection.nb_basedatos
		user = self.connection.id_usuario
		password = self.connection.password
		tns_dsn = cx_Oracle.makedsn(ip, port, sid)
		db = cx_Oracle.connect(user, password, tns_dsn)
		self.cursor = db.cursor();
		print(newSql)
		self.cursor.execute(newSql)
		return self.cursor

	def settingSql(self, sqlOriginal):
		sqlParsed = self.getSqlParsed(sqlOriginal)
		sqlAfterClauseFrom = self.extractSqlAfterClauseFrom(sqlParsed)
		queryFormated =  sqlOriginal.replace(sqlAfterClauseFrom, '')
		where = ConfigWhereClause(self.project)
		queryWithNewWhere = where.getQueryWithNewWhere_Default(queryFormated, sqlParsed)  +' ' + sqlAfterClauseFrom
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