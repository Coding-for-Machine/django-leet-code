from django.contrib import admin
from .models import Problems, Problemtypes, Javoblar
# Register your models here.


@admin.register(Problems)
class ProblemsAdmin(admin.ModelAdmin):
    list_display = ['name',]
@admin.register(Problemtypes)
class ProblemsTypesAdmin(admin.ModelAdmin):
    list_display = ['name',]
@admin.register(Javoblar)
class JavoblarAdmin(admin.ModelAdmin):
    list_display = ['javob',]