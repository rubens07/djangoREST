from .serializers import AutorSerializer, ArtigoSerializer
from rest_framework.permissions import IsAuthenticated
from artigos.models import Autor, Artigo
from rest_framework import viewsets


class AutorViewSet(viewsets.ModelViewSet):
    # IsAuthenticated -> obriga o usuario a estar logado para acessar a api
    # AllowAny -> permite o acesso/inclusao da api por qualquer pessoa
    # IsAuthenticatedOrReadOnly -> permite acesso a api de qualquer pessoa, 
    #   mas apenas usuarios logados podem incluir dados
    permission_classes = (IsAuthenticated, )
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class ArtigoViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated, )
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer
