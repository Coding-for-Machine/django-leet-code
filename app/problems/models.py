from django.db import models

# Create your models here.

class Problemtypes(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Problems(models.Model):
    name = models.CharField(max_length=250)
    problems = models.TextField()
    problemstypes = models.ForeignKey(Problemtypes, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
class Javoblar(models.Model):
    javob = models.TextField()
    problems = models.ForeignKey(Problems, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.javob[:20]