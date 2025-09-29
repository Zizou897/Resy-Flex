# Resy-Flex Landing (Mini Django Project)

Contenu: une mini-app Django `landing` qui expose la landing page à la racine (`/`) avec un formulaire
qui enregistre les leads en base et envoie une notification par email à l'admin.

## Prérequis
- Python 3.8+
- pip

## Installation rapide
1. Crée un environnement virtuel:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / macOS
   venv\Scripts\activate   # Windows
   ```

2. Installe Django:
   ```bash
   pip install django
   ```

3. Depuis le dossier du projet (contenant manage.py), applique les migrations:
   ```bash
   python manage.py migrate
   ```

4. (Optionnel) Crée un superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Lance le serveur:
   ```bash
   python manage.py runserver
   ```

Accède à `http://127.0.0.1:8000/` pour voir la landing page.

## Images
Copie tes images (par ex. `flex5.jpg`, `flex6.jpg`, `flex7.jpg`) dans `static/images/` pour qu'elles s'affichent.

## Email notifications
Par défaut, le projet utilise le backend console (les emails s'affichent dans la console). Pour envoyer de vrais emails,
configure dans `resy_project/settings.py` les variables suivantes:

```py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your-smtp-user'
EMAIL_HOST_PASSWORD = 'your-smtp-password'
EMAIL_USE_TLS = True
EMAIL_FROM = 'no-reply@resy-flex.com'
ADMIN_NOTIFICATION_EMAIL = 'contact@resy-flex.com'
```

## Customisation
- Modifie le template `templates/landing/landing.html`.
- Modifie le modèle `landing/models.py` si tu veux stocker d'autres champs.
