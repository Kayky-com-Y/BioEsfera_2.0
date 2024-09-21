from django.shortcuts import render,redirect
from .models import Usuario,Jogo,Conquista,Conquista_Usuario
# Create your views here.

def index(request):
    return render(request,'BioEsfera/index.html')

def sobre_nos(request):
    return render(request, 'BioEsfera/Sobrenos.html')

# ainda está pegando todos os usuarios
def perfil(request):
    usuario = Usuario.objects.all()
    conquista_usuario = Conquista_Usuario.objects.all()
    contexto = {
        'usuarios': usuario,
        'conquista_usuarios': conquista_usuario,
    }
    return render(request, 'BioEsfera/perfil.html', contexto)

def jornada(request):
    jogo = Jogo.objects.all()
    contexto = {
        'jogos': jogo,
    }
    return render(request, 'BioEsfera/jornada.html', contexto)

def jogos(request, jogo_id):
    jogo_selecionado = Jogo.objects.get(id=jogo_id)
    conquista = Conquista.objects.filter(jogo = jogo_id)
    contexto ={
        'jogo': jogo_selecionado,
        'conquistas': conquista,
    }
    return render(request, 'BioEsfera/jogos.html', contexto)