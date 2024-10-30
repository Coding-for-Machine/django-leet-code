from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from .utils import get_random_code
from django.utils.crypto import get_random_string
# Create your models here.
from register.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    bio = models.CharField(max_length=250, default='O\'zinggiz haqida ...')
    avatar = models.ImageField(default='avatars/avatar.png',upload_to="profile/%Y/%m/%d")
    friends = models.ManyToManyField(CustomUser, null=True, blank=True, related_name='friends')
    slug = models.SlugField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.username)
    
    def save(self, *args, **kwargs):
        now_slug = slugify(str(get_random_string(10, allowed_chars='0123456789'))+ " " +str(id))
        self.slug=now_slug
        return super(Profile, self).save(*args, **kwargs)


STATUS_CHOICES=(
    ('sender', 'sender'),
    ('accepted', 'accepted'),
)
class RelationShip(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.status)
    
    
    