from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(request,'pages/index.html',context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('hire_date')
    # Get realtor of the month
    realtor_of_the_month = Realtor.objects.all().filter(is_mvp= True)
    context = {
        'realtors':realtors,
        'realtor_of_the_month':realtor_of_the_month
    }
    return render(request, 'pages/about.html', context)