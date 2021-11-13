from django.contrib import admin
from .models import Categoria, Dado, Serie


class DadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'numero', 'serie', 'telefone', 'data_nascimento', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'numero', 'serie', 'categoria')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Dado, DadoAdmin)
admin.site.register(Categoria)
admin.site.register(Serie)

