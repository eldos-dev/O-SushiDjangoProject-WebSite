from django.urls import reverse_lazy
from pytils.translit import slugify
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя категории', unique=True)
    slug = models.SlugField(primary_key=True)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products', verbose_name='Изображение')
    additional_information = models.CharField(max_length=50, verbose_name='Порция и вес')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.id})




