from django.shortcuts import render
from .seralizers import ProblemsSerializer, ProblemsTypesSerializer, JavobSerializer, AnswerSerializer
from rest_framework import generics
from problems.models import Problems, Problemtypes, Javoblar
from answer.models import Answer

class ProblemsListCreate(generics.ListCreateAPIView):
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerializer

class ProblemsTypesListCreate(generics.ListCreateAPIView):
    queryset = Problemtypes.objects.all()
    serializer_class = ProblemsTypesSerializer

class JavoblarListCreate(generics.ListCreateAPIView):
    queryset = Javoblar.objects.all()
    serializer_class = JavobSerializer


class AnswerListCreate(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer