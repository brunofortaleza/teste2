from django.contrib.auth.models import User
from django.db import models

class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField('Nome', max_length=128)

    def __str__(self):
        return self.nome

class Agenda(models.Model):
    agenda_publica = models.BooleanField(blank= True, null = True)
    evento = models.CharField('evento', max_length = 128)
    data = models.DateTimeField(blank= True, null = True)
    autor = models.ForeignKey(Pessoa, on_delete = models.CASCADE)
    compromisso = models.TextField()

    def __str__(self):
        return self.evento

class AgendaInstitucional(models.Model):
    publicar = models.BooleanField(blank= True, null = True)
    evento = models.CharField('evento', max_length = 128)
    data = models.DateTimeField(blank= True, null = True)
    autor = models.ForeignKey(Pessoa, on_delete = models.CASCADE)

    def __str__(self):
        return self.evento
