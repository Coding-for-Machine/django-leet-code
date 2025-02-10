from django.db import models
from language.models import Language
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class Problem(models.Model):
    language = models.ManyToManyField(Language,related_name='problems_in_language')
    title = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    description = CKEditor5Field(verbose_name='Darslik yoki Problems', config_name='extends')
    difficulty_choices = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    difficulty = models.CharField(choices=difficulty_choices, max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.title:
            return self.title
        return self.difficulty
    
class Function(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, related_name="functions", on_delete=models.CASCADE)
    function = models.CharField(max_length=250, help_text="def add(a, b):")
    created_at = models.DateTimeField(auto_now_add=True)  # Dars yaratish vaqti
    updated_at = models.DateTimeField(auto_now=True)  # Dars yangilanish vaqti
    def __str__(self):
        return self.function[:30]

class AlgorithmTest(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, related_name="test_cases", on_delete=models.CASCADE)
    algorithm = models.TextField()  # tugri kod kod
    created_at = models.DateTimeField(auto_now_add=True)  # Dars yaratish vaqti
    updated_at = models.DateTimeField(auto_now=True)  # Dars yangilanish vaqti
    def __str__(self):
        return self.algorithm[:30]
    
class TestCase(models.Model):
    algorithm = models.ForeignKey(AlgorithmTest, related_name="test_algorith", on_delete=models.CASCADE)
    input_data = models.CharField(max_length=200)
    output_data = models.CharField(max_length=200)

    def __str__(self):
        return f"Test for {self.algorithm.language.name}"
    


