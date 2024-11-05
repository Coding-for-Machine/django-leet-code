from django.urls import path
from .views import home_page, darslik_page


app_name = "cursapp"

urlpatterns = [
    path("", home_page, name="index"),
    path("dars/", darslik_page, name="darslik"),

]
