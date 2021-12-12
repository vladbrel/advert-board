from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name= 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:ad_list_by_category',args = [self.slug])

class Ad(models.Model):
    name = models.CharField('Название', max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='ads/%Y/%m/%d', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    description = models.TextField('Описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='ads')
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Название'
        verbose_name_plural = 'Названия'
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('main: ad_detail',args = [self.id, self.slug])
