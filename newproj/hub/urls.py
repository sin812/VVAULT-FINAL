from django.urls import path, include

from . import views

from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [ 
path("", views.VinylListView.as_view(), name="index"), #name is useful for constructing urls in templates, dont have to hardcode urls
path("items/", views.AllVinyls.as_view(), name="items"),
path("items/<slug:slug>", views.SingleVinyl.as_view(), name="item-details"),
path('addvinyl/', views.add_vinyl, name='add_vinyl'), #dynamic url pattern #slug helps check if the url is valid
path('addartist/', views.add_artist, name='add_artist'),
path('add_tag/', views.add_tag, name='add_tag'),
path('search/', views.search_vinyls_title, name='search_vinyls_title'),
path('search/tag/', views.search_vinyls_tag, name='search_vinyls_tag'),
path('account/', views.userpage, name='userpage'),
path('changeusername/', views.change_username_view, name='change_username'),
path('profile/', views.user_profile_view, name='profile'),
path('contact/', views.contact_view, name='contact'),
path('manage/', views.manage_content, name='manage_content'),
path('delete_vinyl/<int:pk>/', views.delete_vinyl, name='delete_vinyl'),
path('delete_user/<int:pk>/', views.delete_user, name='delete_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
