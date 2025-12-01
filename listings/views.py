from django.shortcuts import render
from django.views import generic
from .models import Listing


# Create your views here.
class ListingList(generic.ListView):
    model = Listing
    context_object_name = 'listings'
    template_name = 'listings/listing_list.html'
    queryset = Listing.objects.order_by('make')




