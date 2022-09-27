from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Ukol)
class UkolAdmin(admin.ModelAdmin):
    list_display = ["nazev","autor"]