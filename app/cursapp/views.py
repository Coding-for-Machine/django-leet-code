from django.shortcuts import render

# Create your views here.


def home_page(request):
    # problems = Problems.objects.all()
    return render(request, 'home/index.html', {})
def darslik_page(request):
    # problems = Problems.objects.all()
    return render(request, 'curs/language_curses.html', {})
# def LanguageCategory(request):
#     return render(request, "curs/language_curses.html", {})