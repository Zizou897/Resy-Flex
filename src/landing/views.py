from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import LeadForm

def landing(request):
    
    return render(request, 'landing/landing.html', {})
