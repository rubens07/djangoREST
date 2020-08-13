from rest_framework import serializers
from alunos.models import Aluno


# converte Objeto <=> JSON
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

