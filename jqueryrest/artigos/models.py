from django.db import models

# Create your models here.

class Autor(models.Model):

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome
    
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    site = models.URLField(null=True, blank=True)
    email = models.EmailField()
    data_criacao = models.DateTimeField(auto_now_add=True)


class Artigo(models.Model):

    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"

    def __str__(self):
        return self.titulo
    
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    publicado = models.BooleanField(default=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
