from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import *
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    # path('products/', ProductDetailView.as_view(), name='products')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
