from django.core.management import BaseCommand
from catalog.models import *
from config.settings import BASE_DIR
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_data():
        with open('catalog_data.json','r', encoding='utf-8') as file:
            values = json.load(file)
            categories = [item['fields'] for item in values if item['model'] == 'catalog.category']
            products = [item['fields'] for item in values if item['model'] == "catalog.product"]
            return categories, products

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        categories = [{'name': 'Смартфоны', 'description': 'Смартфоны от бюджетных до топовых моделей'},
                    {'name': 'Ноутбуки', 'description': 'Разнообразные ноутбуки для работы и развлечений'},
                    {'name': 'Жесткие диски', 'description': 'Жесткие диски, в том числе внешние и SSD накопители'}
        ]
        products = [{'name': 'Samsung Galaxy A55',
                     'description': 'Смартфон Samsung Galaxy в синем корпусе оснащен дисплеем 6.6. Разрешение 2340x1080 dpi.',
                     'image': None,
                     'category': 'Смартфоны',
                     'price': 500,
                     'created_at': None,
                     'updated_at': None},
                    {'name': 'Apple iPhone 15',
                     'description': 'Модель отличается стильным внешним видом. Корпус Apple iPhone 15 выполнен из алюминия.',
                     'image': None,
                     'category': 'Смартфоны',
                     'price': 700,
                     'created_at': None,
                     'updated_at': None},
                    {'name': 'MSI Katana',
                     'description': 'Ноутбук MSI Katana B12VFK-463XRU создан для погружения в захватывающий виртуальный мир.',
                     'image': None,
                     'category': 'Ноутбуки',
                     'price': 1100,
                     'created_at': None,
                     'updated_at': None},
                    {'name': 'ASUS TUF Gaming',
                     'description': 'Ноутбук ASUS TUF Gaming F15 FX507ZC4-HN009 с диагональю экрана 15.6.',
                     'image': None,
                     'category': 'Ноутбуки',
                     'price': 800,
                     'created_at': None,
                     'updated_at': None},
                    {'name': 'WD Purple Surveillance',
                     'description': 'Создан специально для использования в составе систем видеонаблюдения.',
                     'image': None,
                     'category': 'Жесткие диски',
                     'price': 200,
                     'created_at': None,
                     'updated_at': None},
                    {'name': 'Seagate BarraCuda',
                     'description': 'Скорость передачи данных до 190 Мбайт/сек.',
                     'image': None,
                     'category': 'Жесткие диски',
                     'price': 100,
                     'created_at': None,
                     'updated_at': None},
        ]
        categories_for_db = []
        for category in Command.json_read_data()[0]:
            categories_for_db.append(Category(**category))

        Category.objects.bulk_create(categories_for_db)

        products_for_db = []
        for product in Command.json_read_data()[1]:
            #category_id = Category.objects.get(name=product['category']).id
            product['category'] = Category.objects.get(pk=product['category'])
            products_for_db.append(Product(**product))

        Product.objects.bulk_create(products_for_db)

