from django.shortcuts import render

# Create your views here.


def LanguageCategory(request):
    return render(request, "curs/language_curses.html", {})