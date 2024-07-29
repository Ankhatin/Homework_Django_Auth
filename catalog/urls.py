from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import *
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('products/', ProductListView.as_view(), name='product_list')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
