from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views


from .views import *


urlpatterns = [
    path('', ListListingView.as_view(), name='index'),
    path("create/", ListingFormView.as_view(), name="create"),  
    path('edit/<slug:lis_slug>/', ListingEditView.as_view(), name='edit'),
    path('<slug:lis_slug>/', ListingDetailView.as_view(), name='listing'),
     path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


