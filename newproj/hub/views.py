from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect,get_object_or_404 #importing the render function from django.shortcuts and the get_object_or_404 function which will be used to get the object from the database and return a 404 error if the object is not found
from .models import Vinyl, Artist, Cart, CartItem,Rating #importing the Vinyl and Artist models from the models.py file in the same directory
from django.views.generic import ListView, DetailView
from .forms import VinylForm, ArtistForm, TagForm, EditVinylForm, EditUserForm, UpdateUsernameForm, RateVinylForm, ContactForm #importing the VinylForm and ArtistForm classes from the forms.py file in the same directory
from django.contrib.auth.decorators import login_required
from register.decorators import allowed_users
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from statistics import median
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings





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
    
@login_required
def add_to_cart(request, vinyl_id):
    vinyl = get_object_or_404(Vinyl, id=vinyl_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, vinyl=vinyl)
    
    if not created:
        if cart_item.quantity < vinyl.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f'Added another {vinyl.title} to your cart.')
        else:
            messages.error(request, f'Cannot add more {vinyl.title} to your cart. Only {vinyl.stock} in stock.')
    else:
        if vinyl.stock > 0:
            cart_item.quantity = 1
            cart_item.save()
            messages.success(request, f'Added {vinyl.title} to your cart.')
        else:
            messages.error(request, f'{vinyl.title} is out of stock.')

    return redirect('view_cart')

@login_required
def increase_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if cart_item.quantity < cart_item.vinyl.stock:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'Increased quantity of {cart_item.vinyl.title}.')
    else:
        messages.error(request, f'Cannot add more {cart_item.vinyl.title} to your cart. Only {cart_item.vinyl.stock} in stock.')
    return redirect('view_cart')

@login_required
def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        messages.success(request, f'Reduced quantity of {cart_item.vinyl.title}.')
    else:
        cart_item.delete()
        messages.success(request, f'Removed {cart_item.vinyl.title} from your cart.')
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cartitem_set.all()
    total_price = sum(item.vinyl.price * item.quantity for item in cart_items)
    return render(request, 'hub/cart.html', {'cart': cart, 'cart_items': cart_items, 'total_price': total_price})



@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cartitem_set.all()
    total_price = sum(item.vinyl.price * item.quantity for item in cart_items)
    
    if request.method == 'POST':
        # Get the vinyl IDs before clearing the cart
        purchased_vinyl_ids = list(cart_items.values_list('vinyl_id', flat=True))
        
        # Clear the cart items
        cart_items.delete()
        
        # Ensure only unique vinyl IDs are stored for rating
        request.session['purchased_vinyl_ids'] = list(set(purchased_vinyl_ids))
        
        messages.success(request, 'Thank you for your purchase!')
        
        if purchased_vinyl_ids:
            return redirect('rate_vinyl', vinyl_id=request.session['purchased_vinyl_ids'].pop(0))
        
        return redirect('index')
    
    return render(request, 'hub/checkout.html', {'cart_items': cart_items, 'total_price': total_price})



@login_required
def rate_vinyl(request, vinyl_id):
    vinyl = get_object_or_404(Vinyl, id=vinyl_id)
    
    if request.method == 'POST':
        form = RateVinylForm(request.POST, instance=vinyl)
        if form.is_valid():
            rating_score = form.cleaned_data['rating']
            
            # Check if the user has already rated this vinyl
            if not Rating.objects.filter(vinyl=vinyl, user=request.user).exists():
                Rating.objects.create(vinyl=vinyl, user=request.user, score=rating_score)
                
                # Calculate the median rating
                all_ratings = vinyl.ratings.all().values_list('score', flat=True)
                vinyl.rating = median(all_ratings)
                vinyl.save()
                
                messages.success(request, f'Thank you for rating {vinyl.title}!')
            else:
                messages.warning(request, f'You have already rated {vinyl.title}.')

            # Redirect to the next vinyl to rate or to the index if no more
            if 'purchased_vinyl_ids' in request.session and request.session['purchased_vinyl_ids']:
                next_vinyl_id = request.session['purchased_vinyl_ids'].pop(0)
                if not request.session['purchased_vinyl_ids']:
                    del request.session['purchased_vinyl_ids']
                return redirect('rate_vinyl', vinyl_id=next_vinyl_id)
            
            return redirect('index')
    else:
        form = RateVinylForm(instance=vinyl)
    
    return render(request, 'hub/rate_vinyl.html', {'vinyl': vinyl, 'form': form})


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, f'Removed {cart_item.vinyl.title} from your cart.')
    return redirect(reverse('view_cart'))


@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})