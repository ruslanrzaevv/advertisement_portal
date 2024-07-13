from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import *


urlpatterns = [
    path('', ListListingView.as_view(), name='index'),
    path('<slug:lis_slug>/', ListingDeatilView.as_view(), name='listing'),
    path("create/", ListingFormView.as_view(), name="create")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


