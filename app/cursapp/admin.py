from django.contrib import admin

# Register your models here.
from .models import Bob, Mavzu, Mavzutanasi

admin.site.register(Mavzutanasi)
admin.site.register(Mavzu)

