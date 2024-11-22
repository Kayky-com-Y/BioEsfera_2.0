from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Usuario,Jogo,Conquista,Conquista_Usuario,Imagem_avatar
from .forms import UserContCreationForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,'BioEsfera/index.html')

def sobre_nos(request):
    return render(request, 'BioEsfera/Sobrenos.html')

def perfil(request):
    try:
        usuario = request.user
        conquistas_usuario = Conquista_Usuario.objects.filter(usuario=usuario)
        avatares = Imagem_avatar.objects.all()
        avatar_ids = list(avatares.values_list('id', flat=True))
        avatar_urls = [avatar.imagem.url for avatar in avatares]

        return render(request, 'BioEsfera/perfil.html', {
        'conquistas': conquistas_usuario,
        'usuario': usuario,
        'avatar_ids': avatar_ids,
        'avatar_urls': avatar_urls})

    except Usuario.DoesNotExist:
        return render(request, '404.html', {'message': 'Usuário não encontrado'})

def atualizar_titulo_conquista(request, conquista_id):
    if request.method == 'POST':
        conquista = get_object_or_404(Conquista, id=conquista_id)
        usuario = request.user
        usuario.titulo_conquista = conquista.titulo
        usuario.save()
        return JsonResponse({'status': 'success', 'titulo_conquista': usuario.titulo_conquista})
    return JsonResponse({'status': 'fail'}, status=400)

def atualizar_avatar_usuario(request, avatar_id):
    if request.method == 'POST':
        avatar = Imagem_avatar.objects.get(id=avatar_id)
        usuario = request.user
        usuario.avatar = avatar.imagem
        usuario.save()
        return JsonResponse({'status': 'success', 'avatar_url': usuario.avatar.url})
    return JsonResponse({'status': 'fail'}, status=400)

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticar o usuário
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Loga o usuário
            return redirect('index')  # Redireciona após login
        #else:
            #messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'BioEsfera/login.html')

def logout_view(request):
    logout(request) 
    return redirect('login')  

def cadastro(request):
    if request.method == 'POST':
        form = UserContCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request, 'Cadastro realizado com sucesso! Você já pode fazer login.')
            return redirect('login')  
    else:
        form = UserContCreationForm()

    return render(request, 'BioEsfera/cadastro.html', {'form': form})