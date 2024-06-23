from django.shortcuts import render
from .models import Listing, Category


def home(request):
    listings = Listing.objects.all().order_by('-created_at')[:10]
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'listings': listings,
        'categories': categories,
    })


def search_results(request):
    query = request.GET.get('query')
    location = request.GET.get('location')
    listings = Listing.objects.all()

    if query:
        listings = listings.filter(title__icontains=query)

    context = {
        'listings': listings,
    }

    return render(request, 'search_results.html', context)


def login(request):
    return render(request, 'login.html')
