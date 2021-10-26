from django.contrib import admin
from .models import Categoria, Dado


class DadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'numero', 'serie', 'data_criacao', 'data_nascimento', 'categoria')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'numero', 'serie', 'categoria')


admin.site.register(Categoria)
admin.site.register(Dado, DadoAdmin)

