from django.shortcuts import render
from .models import Listing
from django.views import View

class ListView(View):
    def get(self, request):
        listings = Listing.objects.all()
        return render(request, 'templates/listings/index.html', {'listings': listings})
    

