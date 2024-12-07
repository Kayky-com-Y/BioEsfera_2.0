from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Usuario,Jogo,Conquista,Conquista_Usuario,Imagem_avatar
from django.contrib.auth.decorators import login_required
from .forms import UserContCreationForm, CadastroForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
import json
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib import messages


def index(request):
    return render(request,'BioEsfera/index.html')

def sobre_nos(request):
    return render(request, 'BioEsfera/Sobrenos.html')

@login_required
def perfil(request):
    try:
        usuario = request.user
        conquistas_usuario = Conquista_Usuario.objects.filter(usuario=usuario)
        avatares = Imagem_avatar.objects.all()
        avatar_ids = list(avatares.values_list('id', flat=True))
        avatar_urls = [avatar.imagem.url for avatar in avatares]

        # Configurar a paginação
        paginator = Paginator(conquistas_usuario, 7)  # 10 conquistas por página
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'BioEsfera/perfil.html', {
            'conquistas': page_obj,
            'usuario': usuario,
            'avatar_ids': avatar_ids,
            'avatar_urls': avatar_urls,
            'page_obj': page_obj
        })

    except Usuario.DoesNotExist:
        return render(request, '404.html', {'message': 'Usuário não encontrado'})


def atualizar_conquista_usuario(request, conquista_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            
            usuario = Usuario.objects.get(username=username)
            conquista = get_object_or_404(Conquista, id=conquista_id)
            
            # Atualizar os campos titulo_conquista e descricao_conquista do usuário
            usuario.titulo_conquista = conquista.titulo
            usuario.descricao_conquista = conquista.descricao
            usuario.save()
            
            return JsonResponse({'status': 'success', 'titulo_conquista': usuario.titulo_conquista, 'descricao_conquista': usuario.descricao_conquista})
        except Usuario.DoesNotExist:
            return JsonResponse({'status': 'fail', 'error': 'Usuário não encontrado'}, status=400)
        except Conquista.DoesNotExist:
            return JsonResponse({'status': 'fail', 'error': 'Conquista não encontrada'}, status=400)
        except Exception as e:
            print(f"Erro no servidor: {e}")
            return JsonResponse({'status': 'fail', 'error': str(e)}, status=500)
    return JsonResponse({'status': 'fail', 'error': 'Invalid request method'}, status=400)


def atualizar_avatar_usuario(request, avatar_id):
    if request.method == 'POST':
        avatar = Imagem_avatar.objects.get(id=avatar_id)
        usuario = request.user
        usuario.avatar = avatar.usuario_imagem
        usuario.save()
        return JsonResponse({'status': 'success', 'avatar_url': usuario.avatar.url})
    return JsonResponse({'status': 'fail'}, status=400)

@login_required
def jornada(request):
    jogo = Jogo.objects.all()
    contexto = {
        'jogos': jogo,
    }
    return render(request, 'BioEsfera/jornada.html', contexto)

@login_required
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

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Loga o usuário
            return redirect('perfil')  # Redireciona para a página de perfil
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'BioEsfera/login.html')

def logout_view(request):
    logout(request) 
    return redirect('login')  

def cadastro(request):
    if request.method == 'POST':
        form = UserContCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = UserContCreationForm()

    return render(request, 'BioEsfera/cadastro.html', {'form': form})

def delete_user_view(request):
    if request.method == 'POST':
        user = request.user
        User = get_user_model()
        try:
            User.objects.filter(id=user.id).delete()
            messages.success(request, 'Usuário deletado com sucesso.')
            return redirect('login')  # Redirecionar para a página de login após a deleção
        except Exception as e:
            messages.error(request, f'Erro ao deletar o usuário: {e}')
    return render(request, 'BioEsfera/delete_user_confirm.html')

@csrf_exempt
def login_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'fail', 'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'status': 'fail', 'error': 'Invalid request method'}, status=400)

def obter_csrf_token(request):
    csrf_token = get_token(request)
    response = JsonResponse({'csrfToken': csrf_token})
    response.set_cookie('csrftoken', csrf_token)
    return response

@csrf_exempt
def adicionar_conquista(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            conquista_id = data.get('conquista_id')
            
            usuario = Usuario.objects.get(username=username)
            conquista = Conquista.objects.get(id=conquista_id)
            
            # Verificar se a conquista já existe para o usuário
            if Conquista_Usuario.objects.filter(usuario=usuario, conquista=conquista).exists():
                return JsonResponse({'status': 'fail', 'error': 'Conquista já adicionada para este usuário'}, status=400)
            
            Conquista_Usuario.objects.create(usuario=usuario, conquista=conquista)
            
            return JsonResponse({'status': 'success'})
        except Usuario.DoesNotExist:
            return JsonResponse({'status': 'fail', 'error': 'Usuário não encontrado'}, status=400)
        except Conquista.DoesNotExist:
            return JsonResponse({'status': 'fail', 'error': 'Conquista não encontrada'}, status=400)
        except Exception as e:
            print(f"Erro no servidor: {e}")
            return JsonResponse({'status': 'fail', 'error': str(e)}, status=500)
    return JsonResponse({'status': 'fail', 'error': 'Invalid request method'}, status=400)

@login_required
def atualizar_dados(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados atualizados com sucesso!')
        else:
            messages.error(request, 'Erro ao atualizar dados.')

    else:
        form = CadastroForm(instance=request.user)

    return render(request, 'BioEsfera/atualizar_dados.html', {'form': form})

def conquistas(request):
    conquista = Conquista.objects.all()
    contexto = {
        'conquista': conquista,
    }
    return render(request, 'BioEsfera/conquistas.html', contexto)