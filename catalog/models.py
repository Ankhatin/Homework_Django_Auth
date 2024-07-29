from django.db import models
import psycopg2
from config.settings import DATABASES


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категория')
    description = models.CharField(max_length=200, verbose_name='Описание')

    @classmethod
    def truncate_table(cls):
        conn = psycopg2.connect(database=DATABASES['default']['NAME'],
                                host=DATABASES['default']['HOST'],
                                user=DATABASES['default']['USER'],
                                password=DATABASES['default']['PASSWORD'])
        with conn.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')
        conn.commit()
        conn.close()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Товар')
    description = models.CharField(max_length=200, verbose_name='Описание')
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField(max_length=200, verbose_name='Телефон')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
