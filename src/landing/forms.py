from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['full_name','email','phone','role']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder':'Nom complet','class':'w-full p-2 border rounded'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email','class':'w-full p-2 border rounded'}),
            'phone': forms.TextInput(attrs={'placeholder':'Téléphone','class':'w-full p-2 border rounded'}),
            'role': forms.Select(attrs={'class':'w-full p-2 border rounded'}),
        }
