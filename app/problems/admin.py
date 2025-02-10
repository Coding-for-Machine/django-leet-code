from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Problem, Function, AlgorithmTest, TestCase
from django.utils.html import format_html




# Problem Admin
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'slug', 'created_at')
    search_fields = ('title', 'difficulty')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Problem, ProblemAdmin)


# Function Admin
class FunctionAdmin(admin.ModelAdmin):
    list_display = ('language', 'problem', 'function', 'created_at')
    search_fields = ('language__name', 'problem__title', 'function')
    list_filter = ('language', 'problem')

admin.site.register(Function, FunctionAdmin)



class TestCaseInline(TabularInline):
    model = TestCase
    extra = 4  # Dastlabki yangi TestCase qo'shishni ko'rsatadi

# AlgorithmTest modelini ro'yxatga olish va inline qo'shish
class AlgorithmTestAdmin(admin.ModelAdmin):
    list_display = ('language', 'problem', 'algorithm', 'created_at')
    search_fields = ('language__name', 'problem__title', 'algorithm')
    list_filter = ('language', 'problem')
    inlines = [TestCaseInline]

admin.site.register(AlgorithmTest, AlgorithmTestAdmin)

