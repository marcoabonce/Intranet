from django.db import models

class Area(models.Model):
    title =         models.CharField(max_length=20)
    Descripcion =   models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
