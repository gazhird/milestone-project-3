from django.shortcuts import render
from django.views import generic
from .models import Listing


class ListingList(generic.ListView):
    model = Listing
    context_object_name = 'listings'
    template_name = 'listings/listing_list.html'

    def get_queryset(self):
        queryset = Listing.objects.order_by('make')   # start with everything
        make = self.request.GET.get('make', '').strip()
        if make:
            queryset = queryset.filter(make__icontains=make)
        return queryset
