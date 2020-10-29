from django.db import models
from django.contrib.auth.models import AbstractUser
from area.models import Area
from puesto.models import Puesto

class User(AbstractUser):
    area = models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE)
    puesto = models.ForeignKey(Puesto, null=True, blank=True, on_delete=models.CASCADE)
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
