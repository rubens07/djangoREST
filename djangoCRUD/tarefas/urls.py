from django.urls import path, include
from .views import (
    ListaTarefas, DetalhesTarefa, 
    CreateTarefas, DetailTarefas, 
    AllTarefas
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AllTarefas)


urlpatterns = [
    # Metodo 01
    path('lista/', ListaTarefas.as_view()),
    path('lista/<int:pk>/', DetalhesTarefa.as_view()),
    # Metodo 02
    path('create-tarefas/', CreateTarefas.as_view()),
    path('detail-tarefas/<int:pk>/', DetailTarefas.as_view()),
    # Metodo 03
    path('', include(router.urls)),
]
