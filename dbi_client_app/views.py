from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from .models import *
from .process_project import ConfigProject

def index(request):
	project = DxinProyectos.objects.first()
	newData = ConfigProject(project)
	return HttpResponse(newData.getIndicadoresWithValue())