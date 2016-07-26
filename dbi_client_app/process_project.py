from .indicators import configIndicators
from .project import ConfigProject

class LoadProject():

	def __init__(self, project):
		self.projectToConfig = ConfigProject(project)
		self.indicators = configIndicators(self.projectToConfig)