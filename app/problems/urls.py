from django.urls import path
from .views import ProblemsPage, ProblemList

urlpatterns = [
    path("", ProblemsPage, name='index'),
    path("problems/", ProblemList, name='problemslist'),

]
