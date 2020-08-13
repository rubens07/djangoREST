from rest_framework import viewsets
from alunos.models import Aluno
from .serializers import AlunoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.filter(situacao=True)
    serializer_class = AlunoSerializer
    