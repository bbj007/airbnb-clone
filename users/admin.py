from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .import models 
# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    
    """ Custom User Admin"""
    
    list_display = ("username","email","birthdate","gender","department","position")
    list_filter = ("department","position")

    fieldsets = UserAdmin.fieldsets + ( 
        (
            "Employee Profile",
            { 
                "fields": ( 
                          "photo",
                          "birthdate",
                          "gender",
                          "department",
                          "position", 
                          )        
            },
        ),
    )

