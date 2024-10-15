from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("problems.urls")),
    path('api/', include("api.urls")),
    path('answer/', include("answer.urls")),
    path('profile/', include("profil.urls")),

]
