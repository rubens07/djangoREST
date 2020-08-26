from .serializers import TarefaSerializer
from .models import Tarefa
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status, generics, viewsets


# Create your views here.

# -------------------------
# METODO 01
# -------------------------
class ListaTarefas(APIView):
    def __init__(self):
        super(ListaTarefas, self).__init__()

    def get(self, request):
        lista = Tarefa.objects.all()
        serializer = TarefaSerializer(lista, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class DetalhesTarefa(APIView):
    def __init__(self):
        super(DetalhesTarefa, self).__init__()

    def get_tarefa(self, pk):
        try:
            return Tarefa.objects.get(pk=pk)
        except:
            raise NotFound()
        
    def get(self, request, pk):
        tarefa = self.get_tarefa(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, pk):
        tarefa = self.get_tarefa(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarefa = self.get_tarefa(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------------------------
# METODO 02
# -------------------------
# Classe identica a ListaTarefas
class CreateTarefas(generics.ListCreateAPIView):
    def __init__(self):
        super(CreateTarefas, self).__init__()

    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


# Classe identica a DetalhesTarefa
class DetailTarefas(generics.RetrieveUpdateDestroyAPIView):
    def __init__(self):
        super(DetailTarefas, self).__init__()

    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


# -------------------------
# METODO 03
# -------------------------
# Substitui todas as classes acima
# Necessário criar a variavel "router" em tarefas.urls
class AllTarefas(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
