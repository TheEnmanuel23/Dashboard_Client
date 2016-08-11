import cx_Oracle
from django.db.models import Q
from .server import Server

class ConfigFilters:
	def __init__(self, project):
		self.project = project
		self.server = Server(project.id_conexionbd)

	def getFilters(self):
		filtros = DxinFiltros.objects.filter(Q(id_proyecto = self.project)
		for filtro in filtros:
			print(filtro)
