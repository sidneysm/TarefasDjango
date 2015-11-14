from django.shortcuts import render
from django.utils import timezone
from .models import Tarefa

# Create your views here.
def tarefa_list(request):
	tarefas = Tarefa.objects.all().order_by('nome')
	return render(request, 'core/tarefa_list.html', {'tarefas': tarefas})