from rest_framework import serializers
from problems.models import Problems, Problemtypes, Javoblar
from answer.models import Answer



class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = ['name', 'problems']

class ProblemsTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problemtypes
        fields = ['name']

class JavobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Javoblar
        fields = ["javob", 'problems']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["code", "problems"]