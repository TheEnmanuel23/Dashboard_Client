import cx_Oracle

class Server:
	def __init__(self, DxinConexionConfiguracion_model):
		self.DxinConexionConfiguracion_model = DxinConexionConfiguracion_model

	def settingCursor(self, sqlToExecute):
		serverConfig = self.serverConfigurationData()		
		db = cx_Oracle.connect(serverConfig['user'], serverConfig['password'], serverConfig['tns_dsn'])
		cursor = db.cursor();
		cursor.execute(sqlToExecute)
		return cursor

	def serverConfigurationData(self):
		configurationData = {
			'ip': self.DxinConexionConfiguracion_model.nb_servidor,
			'port': self.DxinConexionConfiguracion_model.nu_puerto,
			'sid': self.DxinConexionConfiguracion_model.nb_basedatos,
			'user': self.DxinConexionConfiguracion_model.id_usuario,
			'password': self.DxinConexionConfiguracion_model.password,
			'tns_dsn': cx_Oracle.makedsn(self.DxinConexionConfiguracion_model.nb_servidor,
										self.DxinConexionConfiguracion_model.nu_puerto,
										self.DxinConexionConfiguracion_model.nb_basedatos)
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