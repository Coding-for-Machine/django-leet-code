from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UpdateUserForm, UpdateProfileForm
from register.models import CustomUser
from .models import Profile

# @login_required
def profile(request):
    if request.user:
        user = get_object_or_404(Profile, user=request.user.id)
    user = None
    return render(request, 'profiles/profile.html', {'user': user})


def profile_edits(request, username):
    user = get_object_or_404(Profile, user=request.user.id)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profiles/profile_edits.html', {'user_form': user_form, 'profile_form': profile_form})