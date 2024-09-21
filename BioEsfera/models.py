from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=150,  unique=True)
    senha = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.nome
    
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
        return self.usuario
