from django.shortcuts import render

# Create your views here.
def ProfilePage(request):
    return render(request, 'user/profile.html', {})

def RegisterPage(request):
    return render(request, 'user/register.html', {})

def LoginPage(request):
    return render(request, "user/login.html", {})

def LogoutPage(request):
    return render(request, 'user/logout.html', {})