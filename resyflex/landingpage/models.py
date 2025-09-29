from django.db import models

class Subscriber(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.email