from django.contrib import admin
from django.urls import include, path
from answer.api import api  # API ni to'g'ri import qilish

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),  # `api.urls` bo'lishi kerak
    path("ckeditor5/", include("django_ckeditor_5.urls")),  # CKEditor 5 uchun URL
    
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)