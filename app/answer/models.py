from django.db import models
from problems.models import Problemtypes, Problems
from django.contrib.auth.models import User
# Create your models here.



class Answer(models.Model):
    code = models.TextField() 
    problems = models.ForeignKey(Problems, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.code
