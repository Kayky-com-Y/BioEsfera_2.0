from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    SEXO_CHOICES = [ ('F','Feminino'), ('M','Masculino'), ('O','Outros'), ('N','Prefiro não dizer')]
    email = models.EmailField(max_length=150)
    idade = models.IntegerField(null=True)
    sexo = models.CharField(max_length=150, choices=SEXO_CHOICES, blank=True)
    titulo_conquista = models.CharField(max_length=150, blank=True, null=True)
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.username
    
class Jogo(models.Model):
    titulo = models.CharField(max_length=150,  unique=True)
    descricao = models.TextField(max_length=1000)
    url = models.CharField(max_length=300)
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Conquista(models.Model):
    titulo = models.CharField(max_length=150,  unique=True)
    descricao = models.TextField(max_length=1000)
    imagem = models.ImageField(upload_to='images/', null=True, blank= True)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Conquista_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conquista = models.ForeignKey(Conquista, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} - {self.conquista.titulo}'
    
class Imagem_avatar(models.Model):
    imagem = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'Avatar {self.id}'

class Usuario_avatar(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    avatar = models.ForeignKey(Imagem_avatar, on_delete=models.CASCADE)
