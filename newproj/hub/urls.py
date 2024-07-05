from django.urls import path

from . import views

from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [ 
path("", views.VinylListView.as_view(), name="index"), #name is useful for constructing urls in templates, dont have to hardcode urls
path("items/", views.AllVinyls.as_view(), name="items"),
path("items/<slug:slug>", views.SingleVinyl.as_view(), name="item-details") #dynamic url pattern #slug helps check if the url is valid
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)