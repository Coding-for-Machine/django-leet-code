from django.contrib import admin
from django.urls import path, include
# from wagtail.admin import urls as wagtailadmin_urls
# from wagtail import urls as wagtail_urls
# from wagtail.documents import urls as wagtaildocs_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("problems/", include('runcode.urls')),
    path("unittest/", include('unittestproblems.urls')),
    path("register/", include('register.urls')),
    path("", include('cursapp.urls')),
    path("profile/", include('profiles.urls')),
    # roter
    path("__reload__/", include("django_browser_reload.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)