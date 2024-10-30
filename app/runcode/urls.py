from django.urls import path
from .views import home_page, code_page, problems_list
from .run import run_code
app_name="runcode"

urlpatterns = [
    path("", home_page, name="index"),
    path("problems/", problems_list, name="problems-list"),
    path("code/<int:id>/<slug:slug>/", code_page, name="run_code"),
    path("api/<str:problem_id>/", run_code),
]

hx_urls=[
    # path("hx/problems/", hx_problems_list, name='hx-problems-list'),

]
urlpatterns += hx_urls