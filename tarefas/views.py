from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def listar_tarefas(request):
    tarefas = Task.objects.all()
    return render (request, 'tarefas/listar.html', {'tarefas': tarefas})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TaskForm()
    return render(request, 'tarefas/criar.html', {'form': form})