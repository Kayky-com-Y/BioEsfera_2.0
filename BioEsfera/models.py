from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    email = models.EmailField(max_length=150, default='Coloque_o_seu_email@email.com')
    idade = models.IntegerField(null=True, default= 18)
    sexo = models.CharField(max_length=150, blank=True, default="Outros")
    titulo_conquista = models.CharField(max_length=150, blank=True, null=True, default="Novato")
    descricao_conquista = models.CharField(max_length=150, blank=True, null=True, default="Aperte em uma conquista que você ganhou e vejá o que acontece ;)")
    avatar = models.ImageField(upload_to='images/', null=True, blank=True, default='images/cebolo_perfil.png')


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
    dica = models.TextField(max_length=1000)
    imagem = models.ImageField(upload_to='images/', null=True, blank= True)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Conquista_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conquista = models.ForeignKey(Conquista, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} - {self.conquista.titulo}'

    class Meta: 
        unique_together = ('usuario', 'conquista')
    
class Imagem_avatar(models.Model):
    imagem = models.ImageField(upload_to='images/')
    usuario_imagem = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'Avatar {self.id}'

class Usuario_avatar(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    avatar = models.ForeignKey(Imagem_avatar, on_delete=models.CASCADE)
