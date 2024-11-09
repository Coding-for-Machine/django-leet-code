from django.contrib import admin

# Register your models here.
from .models import Bob, Mavzu, Mavzutanasi
from .forms import MavzutanasiForms
admin.site.register(Bob)
admin.site.register(Mavzu)
@admin.register(Mavzutanasi)
class MavzutanasiAdmin(admin.ModelAdmin):
    form = MavzutanasiForms


