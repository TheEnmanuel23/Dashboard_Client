from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.
from .models import *
from .process_project import ConfigProject

def index(request):
	project = DxinProyectos.objects.first()
	newData = ConfigProject(project)
	return JsonResponse(newData.getIndicadoresWithValue(), safe=False)

class home(DetailView):
	model = DxinProyectos
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
	    context = super(home, self).get_context_data(**kwargs)
	    self.object = self.get_object()
	    data = ConfigProject(self.object)
	    context['data_table'] = data.getIndicadoresWithValue()
	    context['indicadores_list'] = data.getIndicadoresToShow()
	    return context