from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect,get_object_or_404 #importing the render function from django.shortcuts and the get_object_or_404 function which will be used to get the object from the database and return a 404 error if the object is not found
from .models import Vinyl, Artist
from django.views.generic import ListView, DetailView
from .forms import VinylForm, ArtistForm, TagForm, EditVinylForm, EditUserForm
from django.contrib.auth.decorators import login_required
from register.decorators import allowed_users
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from .forms import UpdateUsernameForm
from django.contrib.auth.models import User









def get_date(vinyl):
    return vinyl["date_added"]



@login_required
def user_profile_view(request):
    user = request.user  # Get the current logged-in user
    if request.method == 'POST':
        form = UpdateUsernameForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Username updated successfully!')
            return redirect('profile')
    else:
        form = UpdateUsernameForm(instance=user)
    
    context = {
        'user': user,  # Pass the user object to the template context
        'form': form,  # Pass the form to the template context
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
@allowed_users(allowed_roles=['PrivUser', 'admin'])
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
@allowed_users(allowed_roles=['PrivUser', 'admin'])
def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace with your desired URL after adding artist
    else:
        form = ArtistForm()
    
    return render(request, 'hub/artistform.html', {'form': form})

@login_required(login_url='login')
def userpage(request):
    return render(request, 'hub/profile.html')

@login_required(login_url='login')
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send an email (for example)
            send_mail(
                f"Message from {name}",
                message,
                email,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            
            return redirect('success')  # Redirect to a success page or display a success message
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['PrivUser', 'admin'])
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace with your desired URL after adding tag
    else:
        form = TagForm()
    
    return render(request, 'hub/tagsform.html', {'form': form})


def search_vinyls_title(request):
    query = request.GET.get('search_query_title', '')
    if query:
        filtered_vinyls = Vinyl.objects.filter(title__icontains=query)
    else:
        filtered_vinyls = Vinyl.objects.all()
    
    context = {
        'allvinyls': filtered_vinyls,
        'artists': Artist.objects.all(),
        'genres': Vinyl.objects.values_list('genre', flat=True).distinct()
    }
    return render(request, 'hub/vinyls.html', context)

def search_vinyls_tag(request):
    query = request.GET.get('search_query_tag', '')
    if query:
        filtered_vinyls = Vinyl.objects.filter(tags__caption__icontains=query).distinct()
    else:
        filtered_vinyls = Vinyl.objects.all()
    
    context = {
        'allvinyls': filtered_vinyls,
        'artists': Artist.objects.all(),
        'genres': Vinyl.objects.values_list('genre', flat=True).distinct()
    }
    return render(request, 'hub/vinyls.html', context)





@login_required
def change_username_view(request):
    user = request.user

    if request.method == 'POST':
        form = UpdateUsernameForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Username updated successfully!')
            return redirect('index')  # Redirect to main page after updating
    else:
        form = UpdateUsernameForm(instance=user)

    context = {
        'form': form,
    }
    return render(request, 'hub/changeusername.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])  # Ensure only admins can access
def manage_content(request):
    vinyls = Vinyl.objects.all()
    users = User.objects.all()
    return render(request, 'hub/manage_content.html', {'vinyls': vinyls, 'users': users})

@login_required
@allowed_users(allowed_roles=['admin'])
def delete_vinyl(request, pk):
    vinyl = get_object_or_404(Vinyl, pk=pk)
    vinyl.delete()
    return redirect('manage_content')

@login_required
@allowed_users(allowed_roles=['admin'])
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('manage_content')

@login_required
@allowed_users(allowed_roles=['admin'])
def edit_vinyl(request, pk):
    vinyl = get_object_or_404(Vinyl, pk=pk)
    if request.method == 'POST':
        form = EditVinylForm(request.POST, request.FILES, instance=vinyl)
        if form.is_valid():
            form.save()
            return redirect('manage_content')
    else:
        form = EditVinylForm(instance=vinyl)
    return render(request, 'hub/editvinyl.html', {'form': form})


@login_required
@allowed_users(allowed_roles=['admin'])
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_content')
    else:
        form = EditUserForm(instance=user)
    return render(request, 'hub/edituser.html', {'form': form})

class AllVinyls(ListView):
    template_name = "hub/vinyls.html"
    model = Vinyl
    context_object_name = "allvinyls"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        artist_id = self.request.GET.get('artist')
        genre = self.request.GET.get('genre')
        search_query_title = self.request.GET.get('search_query_title')
        search_query_tag = self.request.GET.get('search_query_tag')

        if artist_id:
            queryset = queryset.filter(artist_id=artist_id)
        if genre:
            queryset = queryset.filter(genre__icontains=genre)
        if search_query_title:
            queryset = queryset.filter(title__icontains=search_query_title)
        if search_query_tag:
            queryset = queryset.filter(tags__caption__icontains=search_query_tag)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = Artist.objects.all()
        context['genres'] = Vinyl.objects.values_list('genre', flat=True).distinct()
        return context



