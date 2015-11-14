from django.shortcuts import render

# Create your views here.
def tarefa_list(request):
	return render(request, 'core/tarefa_list.html', {})