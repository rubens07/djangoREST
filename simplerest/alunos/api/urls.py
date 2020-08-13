from django.urls import path, include
from rest_framework import routers
from .views import AlunoViewSet


router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# http://localhost:8000/api/alunos/
### Acessa a lista de alunos ativos (devida configuração do queryset em views.py)
### Possibilidade de incluir novos alunos

# http://localhost:8000/api/alunos/X/
### Acessa apenas o aluno com id = X
### Possibilidade de deletar e alterar os dados do aluno
