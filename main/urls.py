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
from django.urls import path, include
from BioEsfera.views import index,sobre_nos,jornada,jogos,perfil,cadastro,login_view,logout_view,atualizar_titulo_conquista, atualizar_avatar_usuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('Sobrenos/', sobre_nos, name='Sobrenos'),
    path('jornada/', jornada, name='jornada'),
    path('jornada/<int:jogo_id>', jogos, name='jogos'),
    path('perfil/', perfil, name='perfil'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cadastro/', cadastro, name='cadastro'),
    path('atualizar_titulo_conquista/<int:conquista_id>/', atualizar_titulo_conquista, name='atualizar_titulo_conquista'),
    path('atualizar_avatar/<int:avatar_id>/', atualizar_avatar_usuario, name='atualizar_avatar'),
]
app_name = 'BioEsfera'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)