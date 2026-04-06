from django.contrib import admin
from .models import Time
 
 
@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'estado', 'criado_em')
    search_fields = ('nome', 'cidade')
    list_filter = ('estado',)
 