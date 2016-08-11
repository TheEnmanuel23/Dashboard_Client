from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.
from .models import *
from .process_project import LoadProject

class home(DetailView):
	model = DxinProyectos
	template_name = 'index.html'
	context_object_name = 'project'

	def get_context_data(self, **kwargs):
	    context = super(home, self).get_context_data(**kwargs)
	    self.object = self.get_object()
	    project = LoadProject(self.object)
	    context['indicadores_list'] = project.indicators.getIndicadoresList()
	    context['indicadores_values'] = project.indicators.getIndicadoresWithValueToLoadPage()
	    return context

class indicadoresTableValues(ListView):
	model = DxinProyectos

	def get(self, request, *args, **kwargs):
		sectionFigureDefault =  request.GET.get('section', None)
		idProject = request.GET.get('idProject', None);
		self.object = DxinProyectos.objects.get(id_proyecto = idProject)
		project = LoadProject(self.object)
		listIndicadores = project.indicators.getIndicadoresWithValueAjax(sectionFigureDefault)
		return self.json_to_response(listIndicadores)

	def json_to_response(self, listIndicadores):
		return JsonResponse(listIndicadores, safe=False)