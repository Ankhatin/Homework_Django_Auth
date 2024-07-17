from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категория')
    description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Товар')
    description = models.CharField(max_length=100, verbose_name='Описание')
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

