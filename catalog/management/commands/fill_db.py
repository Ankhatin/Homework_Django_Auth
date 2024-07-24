from django.core.management import BaseCommand
from catalog.models import *
from config.settings import BASE_DIR
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_data():
        with open('catalog_data.json', 'r', encoding='utf-8') as file:
            values = json.load(file)
            categories = [item['fields'] for item in values if item['model'] == 'catalog.category']
            products = [item['fields'] for item in values if item['model'] == "catalog.product"]
            return categories, products


    def handle(self, *args, **options):
        Category.truncate_table()
        Product.objects.all().delete()
        categories_for_db = []
        for category in Command.json_read_data()[0]:
            categories_for_db.append(Category(**category))

        Category.objects.bulk_create(categories_for_db)

        products_for_db = []
        for product in Command.json_read_data()[1]:
            product['category'] = Category.objects.get(pk=product['category'])
            products_for_db.append(Product(**product))

        Product.objects.bulk_create(products_for_db)

