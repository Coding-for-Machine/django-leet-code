# django_project/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

# forms
from .tokens import account_activation_token
from .forms import PasswordResetForm, SetPasswordForm

# decarotor
from .decorators import user_not_authenticated
from .forms import UserRegistrationForm, UserLoginForm


# Register
# @user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect("/")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request, template_name="users/register.html", context={"form": form}
    )


# User Logout
@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("cursapp:index")


# User alogin


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string(
        "users/template_activate_account.html",
        {
            "user": user.username,
            "domain": get_current_site(request).domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
            "protocol": "https" if request.is_secure() else "http",
        },
    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(
            request,
            f"Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.",
        )
    else:
        messages.error(
            request,
            f"Problem sending confirmation email to {to_email}, check if you typed it correctly.",
        )


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(
            request,
            "Emailni tasdiqlaganingiz uchun tashakkur. Endi siz hisobingizga kirishingiz mumkin.",
        )
        return redirect("register:login")
    else:
        messages.error(request, "Faollashtirish havolasi yaroqsiz!")

    return redirect("register:login")

@user_not_authenticated
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"Assalomu Alaykum <b>{user.username}</b>! Siz tizimga kirgansiz !"
                )
                return redirect("homepage")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = UserLoginForm()

    return render(
        request=request, template_name="users/login.html", context={"form": form}
    )

@login_required
def password_change(request):
    user = request.user
    if request.method == "POST":
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sizning parolingiz o'zgartirildi")
            return redirect("register:login")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, "password_reset_confirm.html", {"form": form})


@user_not_authenticated
def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data["email"]
            associated_user = (
                get_user_model().objects.filter(Q(email=user_email)).first()
            )
            if associated_user:
                subject = "Parolni tiklash so'rovi"
                message = render_to_string(
                    "template_reset_password.html",
                    {
                        "user": associated_user,
                        "domain": get_current_site(request).domain,
                        "uid": urlsafe_base64_encode(force_bytes(associated_user.pk)),
                        "token": account_activation_token.make_token(associated_user),
                        "protocol": "https" if request.is_secure() else "http",
                    },
                )
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(
                        request,
                        """
                        <h2>Parolni tiklash yuborildi</h2><hr>
                        <p>
                            Agar siz kiritgan e-pochtada hisob mavjud boʻlsa, parolni oʻrnatish boʻyicha koʻrsatmalarni elektron pochta orqali yubordik. 
                            Siz ularni tez orada olishingiz kerak.<br>Agar sizga xat olmagan boʻlsa, manzilni kiritganingizga ishonch hosil qiling. 
                            ro'yxatdan o'tgansiz va spam jildini tekshiring.
                        </p>
                        """,
                    )
                else:
                    messages.error(
                        request,
                        "Parolni tiklash e-pochtasini yuborishda muammo, <b>SERVER PROBLEM</b>",
                    )

            return redirect("homepage")
    form = PasswordResetForm()
    return render(
        request=request, template_name="password_reset.html", context={"form": form}
    )


def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    "Parolingiz oʻrnatildi. Siz hozir davom eting va <b>tizimga kiring </b>.",
                )
                return redirect("/")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, "password_reset_confirm.html", {"form": form})
    else:
        messages.error(request, "Havola muddati tugagan")

    messages.error(request, "Nimadir xato ketdi, bosh sahifaga yo‘naltirilmoqda")
    return redirect("/")
