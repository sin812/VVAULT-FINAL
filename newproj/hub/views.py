from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404 #importing the render function from django.shortcuts and the get_object_or_404 function which will be used to get the object from the database and return a 404 error if the object is not found

from datetime import date

from datetime import date

from .models import Vinyl

from django.views.generic import ListView, DetailView



def get_date(vinyl):
    return vinyl["date_added"]




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