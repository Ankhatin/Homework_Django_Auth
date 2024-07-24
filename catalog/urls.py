from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import *
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', product, name='product'),
    path('products/', products, name='products')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
