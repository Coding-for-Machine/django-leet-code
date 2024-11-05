from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnswerForm
from .models import Answer, Problems, Language
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponseRedirect
from .run import run_code
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# run 
# Create your views here.
import time
User = get_user_model()


def hx_home_page(request):
    url_home = reverse('runcode:hx-home-list')
    # problems = Problems.objects.all()
    return render(request, 'home/home_loading.html', {"url_home": url_home})

def problems_list(request):
    user = get_object_or_404(User, id=request.user.id)
    time.sleep(1)
    problems = Problems.objects.all()
    paginator = Paginator(problems, 3)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
    # If page_number is not an integer get the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, "problems/problem_list.html",{"problems": posts, 'user':user})

# def problems_list(request):
#     url = reverse("runcode:hx-problems-list")
#     return render(request, "problems/problems_list.html",{"url": url})

def code_page(request, id, slug):
    context={
    }
    # print("payth", request.path)
    lang = Language.objects.all()
    problem = get_object_or_404(Problems, id=id, slug=slug)
    context["language"]=lang
    context['problem']=problem 
    if request.method=="POST":
        
        # messages.error(request, "rwspons")
        if 'tekshirish' in request.method=="POST":
            pk = request.POST.get('tekshirish')
            print(pk)
            pass
        elif 'save' in request.method=="POST":
            pk = request.POST.get('tekshirish')
            print(pk)
            pass
       
        
        if request.POST.get("code") is not None and request.POST.get('language') is not None and request.user:
            code = request.POST.get('code')
            language = request.POST.get('language')
            lan_filter = Language.objects.get(name=language)
            Answer.objects.create(language=lan_filter,answer=code, problem=problem, user=request.user)
            # return HttpResponseRedirect(reverse(problem.get_absolute_url))
            context['me']="saved"
            return HttpResponse(run_code(request, id))
    if request.htmx:
        return render(request, 'code/create_form_code.html',context )
    return render(request, 'code/code.html',context )

