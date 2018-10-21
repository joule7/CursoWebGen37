from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	'''
	Modelo para almacenar los posts
	'''
	autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)	
	titulo = models.CharField(max_length=200)
	texto = models.TextField()

	fechaCreacion = models.DateTimeField(default = timezone.now)
	fechaPublicacion = models.DateTimeField(blank = True, null = True)

	def publicar(self):
		'''
		Función para obtener la fecha de publicación
		cuando se publique algún Post
		'''	
		self.fechaPublicacion = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo
