from django.urls import path
from .views import ProblemsListCreate, ProblemsTypesListCreate, JavoblarListCreate, AnswerListCreate


urlpatterns = [
    path("", ProblemsListCreate.as_view()), 
    path("problem-type/", ProblemsTypesListCreate.as_view()),
    path("javoblar/", JavoblarListCreate.as_view()),
    path("code/", AnswerListCreate.as_view()),
]
