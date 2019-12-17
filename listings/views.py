from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings':paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing':listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    query_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains= keywords)
    # City
    if 'cirty' in request.GET:
        # City is the name of the field
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)
    # State
    if 'state' in request.GET:
        # state is the name of the field
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)
    # Bedrooms
    if 'bedrooms' in request.GET:
        # bedrooms is the name of the field
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            # Less then
            query_list = query_list.filter(bedrooms__lte=bedrooms)
    # Price
    if 'price' in request.GET:
        # bedrooms is the name of the field
        price = request.GET['price']
        if price:
            # Less then
            query_list = query_list.filter(price__lte=price)
    context = {
        'listings': query_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
