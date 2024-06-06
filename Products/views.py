from django.shortcuts import render
from .models import Listing

def home(request):
    listings = Listing.objects.all().order_by('-created_at')[:10]
    return render(request, 'home.html', {'listings': listings})