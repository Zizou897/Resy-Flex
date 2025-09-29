from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','phone','role','created_at')
    list_filter = ('role','created_at')
    search_fields = ('full_name','email','phone')
