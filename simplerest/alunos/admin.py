from django.contrib import admin
from .models import Aluno
# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    class Meta:
        model = Aluno

    list_display = ('nome', 'email', 'curso', 'situacao', 'ultima_atualizacao')
    list_filter = ('curso', 'situacao')


admin.site.register(Aluno, AlunoAdmin)
