from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.VinylListView.as_view(), name="index"),  # Also handles filtering if adapted
    path("items/", views.AllVinyls.as_view(), name="items"),  # Reused for simplicity
    path("items/<slug:slug>", views.SingleVinyl.as_view(), name="item-details"),
    path('addvinyl/', views.add_vinyl, name='add_vinyl'),
    path('addartist/', views.add_artist, name='add_artist'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('search/', views.search_vinyls_title, name='search_vinyls_title'),
    path('search/tag/', views.search_vinyls_tag, name='search_vinyls_tag'),
    path('account/', views.userpage, name='userpage'),
    path('changeusername/', views.change_username_view, name='change_username'),
    path('profile/', views.user_profile_view, name='profile'),
    path('contact/', views.contact_view, name='contact'),
    path('manage/', views.manage_content, name='manage_content'),
    path('edit_vinyl/<int:pk>/', views.edit_vinyl, name='edit_vinyl'),
    path('edit_user/<int:pk>/', views.edit_user, name='edit_user'),
    path('delete_vinyl/<int:pk>/', views.delete_vinyl, name='delete_vinyl'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
