from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',register,name="register"),
    path('register',register,name="register"),
    path('login',login,name="login"),
    path('fileupload',fileupload,name="fileupload"),
    path('recentlyuploaded',recentlyuploaded,name="recentlyuploaded"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)