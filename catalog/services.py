from django.core.cache import cache

from catalog.models import Category
from config import settings


def get_cached_categories():
    if settings.CACHE_ENABLED:
        subject_list = cache.get('category_list')
        if subject_list is None:
            subject_list = Category.objects.all()
            cache.set('category_list', subject_list)
    else:
        subject_list = Category.objects.all()
    return subject_list
