from django.urls import path
from .views import LanguageCategory

urlpatterns = [
    path("", LanguageCategory, name='categoryalanguage'),
    
]
