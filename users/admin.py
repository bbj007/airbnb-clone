from django.contrib import admin
from .import models 
# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
    
    """ Custom User Admin"""
    
    list_display = ("username","email","birthdate","gender","department","position")
    list_filter = ("department","position")
