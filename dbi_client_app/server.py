import psycopg2

class Server(IServer):
	def __init__(self, DxinConexionConfiguracion_model):
		self.DxinConexionConfiguracion_model = DxinConexionConfiguracion_model

	def settingCursor(self, sqlToExecute):
		serverConfig = self.serverConfigurationData()
		db = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s'" % serverConfig['ip'],
		serverConfig['dbname'], serverConfig['user'], serverConfig['password'])
		cursor = db.cursor()
		cursor.execute(sqlToExecute)
		return cursor

	def serverConfigurationData(self):
		configurationData = {
			'ip': self.DxinConexionConfiguracion_model.nb_servidor,
			'port': self.DxinConexionConfiguracion_model.nu_puerto,
			'user': self.DxinConexionConfiguracion_model.id_usuario,
			'password': self.DxinConexionConfiguracion_model.password,
			'dbname': self.DxinConexionConfiguracion_model.nb_basedatos
		}
		return configurationData

	def convertCursorToList(cursor):
		dictData = list()
		column_names = Server.getColumnsDescriptions(cursor)
		for row in cursor:
			dictData.append(dict(zip(column_names, row)))
		return dictData

	def getColumnsDescriptions(cursor):
		columns = [col[0] for col in cursor.description]
		return columns

	def getDataOfCursor(self, cursor):
		tupleOfResult= tuple()
		for result in cursor:
			tupleOfResult += result
		return tupleOfResult