from django.db import models

# Create your models here.
#https://django.fun/ru/docs/django/4.1/ref/models/fields/#field-types

class Product(models.Model):

    name = models.CharField(max_length=50, null=True, unique=True, verbose_name='Наименование')
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )
    cash = models.IntegerField(null=False, verbose_name='Цена')
    row = models.IntegerField(null=False, verbose_name='Ряд')
    sale = models.IntegerField(null=True, verbose_name='Скидка')
    cnt = models.IntegerField(null=True, verbose_name='Количество', default=0)
    dater = models.DateField(null=False, verbose_name='Дата изготавления', default='2023-02-08')
    image = models.ImageField(upload_to='', default='static/images/placeholder.png')

    def __str__(self):
        return f'{self.name}, {self.category}'
         
        

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name

class Order(models.Model):
    email = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=11, verbose_name='Номер телефона')
    cnt = models.CharField(max_length=3, verbose_name='Количество')
    product = models.ForeignKey(
        'Product',
        on_delete=models.DO_NOTHING,
        null=False,
        verbose_name='Продукт'
    )
