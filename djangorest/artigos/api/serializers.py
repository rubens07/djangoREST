from artigos.models import Autor, Artigo
from rest_framework import serializers


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
        

class ArtigoSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()
    class Meta:
        model = Artigo
        fields = ('titulo', 'texto', 'data_publicacao', 'autor')
