from django.db import models

# Create your models here.
class Studentlist(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    address = models.CharField(max_length=120)

    def __str__(self):
        return self.name