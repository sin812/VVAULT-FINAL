
from django.contrib import admin
from django.urls import path, include
from register import views as v



urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"), #register url
    path("logout/", v.logout_view, name="logout"), #logout url
    path("login/", v.login_view, name="login"), #login url
    path("userpage/", v.userpage, name="userpage"), #userpage url
    path('', include("django.contrib.auth.urls")), #include all the urls from django.contrib.auth.urls
    path("", include('hub.urls')), #include all the urls from hub.urls
] 

