from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import *


urlpatterns = [
    path('', ListView.as_view(), name='index')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


