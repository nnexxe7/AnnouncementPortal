from django.shortcuts import render
from .models import Listing, Category


def home(request):
    listings = Listing.objects.all().order_by('-created_at')[:10]
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'listings': listings,
        'categories': categories,
    })