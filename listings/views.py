from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.text import slugify

from .models import Listing, Category
from .forms import ListingForm

class ListListingView(View):
    def get(self, request):
        listings = Listing.objects.all() 
        categories = Category.objects.all()

        if request.GET.get('category'):
            cat_slug = request.GET.get('category')

            category = Category.objects.get(slug=cat_slug)
            listings = Listing.objects.filter(category=category)
        else:
            listings = Listing.objects.all() 


        context = {
            'listings': listings,
            'categories': categories
            }
        return render(request, 'listings/index.html', context)  
    
class ListingDetailView(View):
    def get(self, request, lis_slug):
        listing = get_object_or_404(Listing, slug=lis_slug) 
        return render(request, 'listings/listing_detail.html', {'listing': listing})


@method_decorator(login_required, name='dispatch')
class ListingFormView(View):
    def get(self, request):
        form = ListingForm()
        return render(request, 'listings/lis_form.html', {'form': form})
    
    def post(self, request):
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.slug = slugify(listing.title)
            listing.save()
            form.save_m2m()
            return redirect('listing', lis_slug=listing.slug) 
        return render(request, 'listings/lis_form.html', {'form': form})

class ListingEditView(View):
    def get(self, request, lis_slug):
        listing = get_object_or_404(Listing, slug=lis_slug) 
        form = ListingForm(instance=listing)
        return render(request, 'listings/lis_form.html', {'form': form})
    
    def post(self, request, lis_slug):
        listing = get_object_or_404(Listing, slug=lis_slug)  
        form = ListingForm(request.POST,request.FILES, instance=listing )
        if form.is_valid():
            form.save()
            return redirect('listing', lis_slug=listing.slug)  
        return render(request, 'listings/lis_form.html', {'form': form})