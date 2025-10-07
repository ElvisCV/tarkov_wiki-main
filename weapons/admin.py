from django.contrib import admin
from .models import Weapon

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name', 'description')
    list_filter = ('created', 'updated')
    readonly_fields = ('created', 'updated')
    
    fieldsets = (
        ('Información del Arma', {
            'fields': ('name', 'description', 'img')
        }),
        ('Metadatos', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )