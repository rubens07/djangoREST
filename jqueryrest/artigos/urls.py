from django.urls import path
from artigos import views


urlpatterns = [
    path('', views.home),
    path('publicacoes/', views.publicacoes),
]
