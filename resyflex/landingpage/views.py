from django.shortcuts import render, redirect
from .models import Subscriber
from django.contrib import messages

def index(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')

        if nom and email and telephone:
            if Subscriber.objects.filter(email=email).exists():
                messages.error(request, 'Cette adresse e-mail est déjà inscrite.')
            else:
                subscriber = Subscriber(nom=nom, email=email, telephone=telephone)
                subscriber.save()
                messages.success(request, 'Merci pour votre inscription !')
                return redirect('index')
        else:
            messages.error(request, 'Veuillez remplir tous les champs.')

    return render(request, "landingpage/index.html")