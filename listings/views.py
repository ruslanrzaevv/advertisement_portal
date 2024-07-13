from django.shortcuts import render, get_object_or_404  , redirect
from django.views import View

from .models import Listing
from .forms import ListingForm


class ListListingView(View):
    def get(self, request):
        listing = Listing.objects.all()
        return render(request, 'listings/index.html', {'listing': listing})   
    
class ListingDeatilView(View):
    def get(self, request, lis_slug):
        listing = get_object_or_404(Listing, slug=lis_slug)
        return render(request, 'listings/listing_detail.html', {'listing':listing})


class ListingFormView(View):
    def get(self, request):
        form = ListingForm()
        return render(request, 'listings/lis_form.html', {'form': form})
    
    def post(self, request):
        form = ListingForm(request.POST)  

        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            return redirect('listing', slug=listing.slug)  
        return render(request, 'listings/lis_form.html', {'form':form})