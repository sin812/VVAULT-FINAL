from django.urls import path

from . import views

urlpatterns = [ 
path("", views.index, name="index"), #name is useful for constructing urls in templates, dont have to hardcode urls
path("items/", views.items, name="items"),
path("items/<slug:slug>", views.item_details, name="item-details") #dynamic url pattern #slug helps check if the url is valid
]