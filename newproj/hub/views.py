from django.shortcuts import render, get_object_or_404 #importing the render function from django.shortcuts and the get_object_or_404 function which will be used to get the object from the database and return a 404 error if the object is not found

from datetime import date

from datetime import date

from .models import Vinyl



def get_date(vinyl):
    return vinyl["date_added"]




# Create your views here.

def index(request):
    new_vinyls=Vinyl.objects.all().order_by("-price")[:2] #will convert the statement to a query that will get the first two items in the database
    return render(request, "hub/index.html", {"vinyls": new_vinyls}) #rendering the index.html template


def items(request):
    allvinyls=Vinyl.objects.all().order_by("-price") #will convert the statement to a query that will get all the items in the database
    return render(request, "hub/vinyls.html", {"allvinyls": allvinyls}) #rendering the items.html template 

def item_details(request, slug): #slug is the parameter that is passed from the url
    vinylid=get_object_or_404(Vinyl,slug=slug) #will convert the statement to a query that will get the item with the slug passed in the url
    return render(request,"hub/vinyldetail.html", {"vinyl":vinylid,"vinyltags":vinylid.tags.all()}) #rendering the item_detail.html template