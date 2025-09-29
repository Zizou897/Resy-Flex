from django.db import models

class Lead(models.Model):
    ROLE_CHOICES = [
        ('voyageur','Voyageur'),
        ('proprietaire','Propriétaire'),
        ('ambassadeur','Ambassadeur'),
    ]
    full_name = models.CharField('Nom complet', max_length=150)
    email = models.EmailField('Email')
    phone = models.CharField('Téléphone', max_length=30, blank=True)
    role = models.CharField('Rôle', max_length=20, choices=ROLE_CHOICES, default='voyageur')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} — {self.email}"
