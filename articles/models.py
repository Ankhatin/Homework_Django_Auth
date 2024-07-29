from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug')
    body = models.CharField(max_length=100, verbose_name='Содержание')
    preview = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    count_review = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ['title', 'is_published', 'count_review']
