from django.contrib import admin
from .models import Usuario,Jogo,Conquista,Conquista_Usuario
from django.utils.html import format_html
# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display =['nome']

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display=['titulo','imagem']

@admin.register(Conquista)
class ConquistaAdmin(admin.ModelAdmin):
    list_display=['titulo']

@admin.register(Conquista_Usuario)
class Conquista_UsuarioAdmin(admin.ModelAdmin):
    list_display=['usuario']