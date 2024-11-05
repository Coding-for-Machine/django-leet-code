from django.urls import path
from .views import home_page


app_name = "cursapp"

urlpatarens = [
    path("", home_page, name="index"),
]