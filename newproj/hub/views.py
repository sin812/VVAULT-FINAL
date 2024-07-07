from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404 #importing the render function from django.shortcuts and the get_object_or_404 function which will be used to get the object from the database and return a 404 error if the object is not found

from datetime import date

from datetime import date

from .models import Vinyl

from django.views.generic import ListView, DetailView

from .forms import VinylForm, ArtistForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from register.decorators import allowed_users







def get_date(vinyl):
    return vinyl["date_added"]



@login_required
def user_profile_view(request):
    user = request.user  # Get the current logged-in user
    context = {
        'user': user  # Pass the user object to the template context
    }
    return render(request, 'profile.html', context)


# Create your views here.


class AllVinyls(ListView):
    template_name = "hub/vinyls.html"    
    model = Vinyl
    ordering = ["-price"]
    context_object_name = "allvinyls"

class VinylListView(ListView):
    template_name = "hub/index.html"
    model = Vinyl
    ordering = ["-price"]
    context_object_name = "vinyls"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        data=queryset[:2]
        return data


class SingleVinyl(DetailView):
    template_name = "hub/vinyldetail.html"
    model = Vinyl

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vinyl_tags"] = self.object.tags.all()
        return context
    

@login_required(login_url='login')
@allowed_users(allowed_roles=['PrivUser'])
def add_vinyl(request):
    if request.method == 'POST':
        form = VinylForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('items')  # Replace with your URL name for vinyl list view
    else:
        form = VinylForm()
    
    return render(request, 'hub/form.html', {'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['PrivUser'])
def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace with your desired URL after adding artist
    else:
        form = ArtistForm()
    
    return render(request, 'hub/artistform.html', {'form': form})