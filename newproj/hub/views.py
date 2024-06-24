from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "hub/index.html") #rendering the index.html template

def items(request):
    pass

def item_details(request):
    pass #rendering the item_detail.html template