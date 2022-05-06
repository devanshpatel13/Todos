from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Todo)
class Todoadmin(admin.ModelAdmin):
    list_display = ["title","descripation","date"]