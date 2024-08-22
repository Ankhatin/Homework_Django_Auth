from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from catalog.views import *
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category', CategoryListView.as_view(), name='category'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
