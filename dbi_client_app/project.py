import cx_Oracle, sqlparse
from dbi_client_app.models import *
from sqlparse.sql import Where
from sqlparse.tokens import Keyword

class ConfigProject():
	def __init__(self, projectToConfig):
		self.project = projectToConfig
		self.connection = self.project.id_conexionbd
		self.setCursor()

	def setCursor(self):
		sql = self.project.sql		
		self.settingWhere(sql)

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

	def settingWhere(self, sqlOriginal):
		sqlParsed = sqlparse.parse(sqlOriginal)[0]
		originalWhere = self.getWhere(sqlParsed)
		if(originalWhere):
			whereCloned = str(originalWhere)
			filtros = DxinFiltros.objects.filter(id_proyecto = self.project)
			for filtro in filtros:
				newWhere = None
				if(filtro.in_defecto.upper() ==  'S' ):
					newWhere = ' and ' + filtro.id_columna + " = '%s'" % filtro.valor_defecto
				if(newWhere):
					whereCloned += str(newWhere)

			print(whereCloned)
		elif self.sql_isGrouped(sqlParsed):
			print('is grouped')
		else:
			print('ehhh more easy')

	def extract_groupBy(self, sqlParsed):
		for token in sqlParsed:
			if token.ttype is Keyword and token.value.upper() == 'GROUP':
				print(token)

	def sql_isGrouped(self, sqlParsed):
		isGrouped = False
		for token in sqlParsed:
			if token.ttype is Keyword and token.value.upper() == 'GROUP':
				isGrouped = True
				break
		return isGrouped

	def getWhere(self, sqlParsed):
		where = None
		for token in sqlParsed:
			if isinstance(token, Where):
				where = token
				break

		return where
