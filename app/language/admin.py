from django.contrib import admin
from .models import Language

# Register your models here.


# Language Admin
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'id')  # Ko'rsatiladigan ustunlar
    search_fields = ('name', 'slug')  # Qidiruvni faollashtirish
    list_filter = ('name',)  # Filtrlar qo'shish
    prepopulated_fields = {'slug': ('name',)}  # Slugni avtomatik to'ldirish

admin.site.register(Language, LanguageAdmin)