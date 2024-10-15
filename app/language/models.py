from django.db import models

# Create your models here.

class Language(models.Model):
    language = models.CharField(max_length=250)
    docker_image = models.CharField(max_length=250)
    cmd = models.CharField(max_length=250)
    

    def __str__(self):
        return self.language
    