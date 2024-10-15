from django.shortcuts import render
import time
# Create your views here.


def ProblemsPage(request):
    time.sleep(1)
    # if request.htmx:
    return render(request, 'home.html', {})
    # return render(request, "home_full.html", {})


def ProblemList(request):
    time.sleep(1)
    return render(request, 'problems/problem_list.html', {})