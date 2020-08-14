from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'artigos/autores.html')


def publicacoes(request):
    return render(request, 'artigos/artigos.html')
