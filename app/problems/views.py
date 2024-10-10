from django.shortcuts import render

# Create your views here.


def ProblemsPage(requests):
    return render(requests, 'home.html', {})