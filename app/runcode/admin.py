from django.contrib import admin
from .models import  Problems, Answer, Comments, Tage, Category, Language, Unittestproblem, Algorithm
from .forms import ProblemsForms
# Register your models here.

# problems admin 
class ProblemsAdmin(admin.ModelAdmin):
    form = ProblemsForms
admin.site.register(Problems, ProblemsAdmin)
admin.site.register(Answer)
admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(Tage)
admin.site.register(Language)
admin.site.register(Unittestproblem)
admin.site.register(Algorithm)



