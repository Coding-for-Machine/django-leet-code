from django.urls import path
from .views import ProblemsPage

urlpatterns = [
    path("", ProblemsPage, name='problem-page'),
]
