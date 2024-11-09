from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class CoursecategoryManager(models.Manager):
    def get_queryset(self):
        return super(Coursecategory, self).get_queryset().filter(active=True)

class Coursecategory(models.Model):
    title = models.CharField(max_length=250, help_text="Dasturlash Tilini yoki Boshqa")
    body = CKEditor5Field()
    active = models.BooleanField(default=True)
    objects = models.Manager()
    published = CoursecategoryManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class BobManager(models.Manager):
    def get_queryset(self):
        return super(Coursecategory, self).get_queryset().filter(active=True)
    
class Bob(models.Model):
    title = models.CharField(max_length=250, help_text="Dasturlash Tilini yoki Boshqa")
    body = CKEditor5Field()
    coursecategory = models.ForeignKey(Coursecategory, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    published = CoursecategoryManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class MavzuManager(models.Manager):
    def get_queryset(self):
        return super(Coursecategory, self).get_queryset().filter(active=True)

class Mavzu(models.Model):
    title = models.CharField(max_length=250, help_text="Dasturlash Tilini yoki Boshqa")
    body = CKEditor5Field()
    bob = models.ForeignKey(Bob, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    published = MavzuManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class MavzutanasiManager(models.Manager):
    def get_queryset(self):
        return super(Coursecategory, self).get_queryset().filter(active=True)

class Mavzutanasi(models.Model):
    title = models.CharField(max_length=250, help_text="Dasturlash Tilini yoki Boshqa")
    body = CKEditor5Field()
    bob = models.ForeignKey(Bob, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    published = MavzutanasiManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    