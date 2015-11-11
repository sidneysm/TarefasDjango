from django.db import models
from django.utils import timezone

# Create your models here.
class Tarefa(models.Model):

	nome = models.CharField(max_length=200)
	descricao = models.CharField(max_length=256)
	prazo = models.DateTimeField(default=timezone.now())
	realizada = models.BooleanField()

	def __str__(self):
		return self.nome