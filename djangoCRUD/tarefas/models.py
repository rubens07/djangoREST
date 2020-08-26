from django.db import models

# Create your models here.

class Tarefa(models.Model):

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return self.nome
    
    nome = models.CharField(max_length=150)
    feito = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    