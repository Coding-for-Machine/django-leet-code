from django.contrib import admin
from .models import Problemimage, Problems, Answer, Comments, Tage, Category, Language, Unittestproblem, Algorithm

# Register your models here.


admin.site.register(Problems)
admin.site.register(Problemimage)
admin.site.register(Answer)
admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(Tage)
admin.site.register(Language)
admin.site.register(Unittestproblem)
admin.site.register(Algorithm)



