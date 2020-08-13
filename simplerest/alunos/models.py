from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Aluno(models.Model):

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return self.nome
    
    nome = models.CharField(max_length=50)
    idade = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    curso = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    situacao = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    