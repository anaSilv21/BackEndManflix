from django.contrib import admin
from .models import *

class detAssinatura(admin.ModelAdmin):
    list_display = ('id','nome', 'valor',)
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10
class detUsuarios(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'cpf', 'fone', 'nascimento','idUserFK', 'idAssinaturaFK')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10
class detCategoria(admin.ModelAdmin):
    list_display = ('id','nome', )
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10
class detFilmes(admin.ModelAdmin):
    list_display = ('id','nome', 'foto','banner','logo','descricao', 'idCategoriaFK')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10
class detFavoritos(admin.ModelAdmin):
    list_display = ('id','idFilmeFK', 'idUsuarioFK',)
    list_display_links = ('id',)
    list_per_page = 10

admin.site.register(Assinatura, detAssinatura)
admin.site.register(Usuarios, detUsuarios)
admin.site.register(Categoria, detCategoria)
admin.site.register(Filmes, detFilmes)
admin.site.register(Favoritos, detFavoritos)
