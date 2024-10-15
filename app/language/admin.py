from django.contrib import admin
from .models import Language

# Register your models here.


class LanguageAdmin(admin.ModelAdmin):
    list_display = ["language", "cmd"]
admin.site.register(Language)