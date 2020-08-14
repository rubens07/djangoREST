from django.contrib import admin
from .models import Artigo, Autor

# Register your models here.

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao', 'ultima_atualizacao', 'publicado')
    
    class Meta:
        model = Artigo


admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Autor)
