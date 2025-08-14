from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from datetime import date


class ListarTarefasView(ListView):
    model = Task
    template_name = 'tarefas/listar.html'
    context_object_name = 'tarefas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        context['pendentes_count'] = Task.objects.filter(done=False).count()
        context['concluidas_count'] = Task.objects.filter(done=True).count()
        context['total_count'] = Task.objects.count()
        return context

class ListarTarefasPendentesView(ListView):
    model = Task
    template_name = 'tarefas/listar.html'
    context_object_name = 'tarefas'

    def get_queryset(self):
        return Task.objects.filter(done=False)

class ListarTarefasConcluidasView(ListView):
    model = Task
    template_name = 'tarefas/listar.html'
    context_object_name = 'tarefas'

    def get_queryset(self):
        return Task.objects.filter(done=True)

class CriarTarefaView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tarefas/criar.html'
    success_url = reverse_lazy('listar_tarefas')

class EditarTarefaView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tarefas/editar.html'
    success_url = reverse_lazy('listar_tarefas')

class ExcluirTarefaView(DeleteView):
    model = Task
    template_name = 'tarefas/excluir.html'
    success_url = reverse_lazy('listar_tarefas')

def alternar_status(request, id):
    tarefa = get_object_or_404(Task ,id=id)
    tarefa.done = not tarefa.done
    tarefa.save()
    return redirect('listar_tarefas')

def limpar_tarefas_concluidas(request):
    Task.objects.filter(done=True).delete()
    return redirect('listar_tarefas')