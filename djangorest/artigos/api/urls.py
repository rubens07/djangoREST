from .views import AutorViewSet, ArtigoViewSet
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('autor', AutorViewSet)
router.register('artigo', ArtigoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
