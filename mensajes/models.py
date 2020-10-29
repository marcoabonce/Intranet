from django.db import models

# Create your models here.
class Mensaje(models.Model):
    title =         models.CharField(max_length=20)
    mensaje =       models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

    def get_mensajes(self):
        mensajes = Mensaje.objects.all()
        return mensajes