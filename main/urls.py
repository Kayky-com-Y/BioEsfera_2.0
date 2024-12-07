"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from BioEsfera.views import index,sobre_nos,jornada,jogos,perfil,cadastro,login_view,logout_view,atualizar_conquista_usuario, atualizar_avatar_usuario, login_usuario, obter_csrf_token, adicionar_conquista,atualizar_dados, conquistas, delete_user_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('Sobrenos/', sobre_nos, name='Sobrenos'),
    path('jornada/', jornada, name='jornada'),
    path('jornada/<int:jogo_id>', jogos, name='jogos'),
    path('perfil/', perfil, name='perfil'),
    path('conquistas/', conquistas, name='conquistas'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cadastro/', cadastro, name='cadastro'),
    path('delete/', delete_user_view, name='delete_user'),
    path('atualizar_conquista_usuario/<int:conquista_id>/', atualizar_conquista_usuario, name='atualizar_conquista_usuario'),
    path('atualizar_avatar/<int:avatar_id>/', atualizar_avatar_usuario, name='atualizar_avatar'),
    path('login_usuario/', login_usuario, name='login_usuario'),
    path('obter_csrf_token/', obter_csrf_token, name='obter_csrf_token'),
    path('adicionar_conquista/', adicionar_conquista, name='adicionar_conquista'),
    path('atualizar_dados/', atualizar_dados, name='atualizar_dados'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
