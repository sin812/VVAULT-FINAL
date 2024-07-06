
from django.contrib import admin
from django.urls import path, include
from register import views as v



urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"), #register url
    path('', include("django.contrib.auth.urls")), #include all the urls from django.contrib.auth.urls
    path("", include('hub.urls')), #include all the urls from hub.urls
]

