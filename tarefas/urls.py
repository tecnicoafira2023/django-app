from django.urls import path
from django.shortcuts import redirect
from .views import (
    ListarTarefasView, CriarTarefaView, EditarTarefaView, ExcluirTarefaView,
    alternar_status, limpar_tarefas_concluidas,
    ListarTarefasPendentesView, ListarTarefasConcluidasView
)

urlpatterns = [
    path('', ListarTarefasView.as_view(), name='listar_tarefas'),
    path('pendentes/', ListarTarefasPendentesView.as_view(), name='listar_tarefas_pendentes'),
    path('concluidas/', ListarTarefasConcluidasView.as_view(), name='listar_tarefas_concluidas'),
    path('criar/', CriarTarefaView.as_view(), name='criar_tarefa'),
    path('editar/<int:pk>/', EditarTarefaView.as_view(), name='editar_tarefa'),
    path('excluir/<int:pk>/', ExcluirTarefaView.as_view(), name='excluir_tarefa'),
    path('alternar/<int:id>/', alternar_status, name='alternar_status'),
    path('limpar_concluidas/', limpar_tarefas_concluidas, name='limpar_concluidas'),
]
