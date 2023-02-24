from django.contrib import admin
from .models import Product, Category, Order
from django.shortcuts import resolve_url
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.utils.html import format_html

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cash', 'row', 'sale', 'category_display', 'cnt', 'dater']

    def category_display(self, product: Product):
        if product.category is None:
            return '-'

        category = (resolve_url(
        admin_urlname(Category._meta, 'change'),
        product.category.pk
        ), product.category.name)

        return format_html(
            f'<a href="{category[0]}">'
            + f'{category[1]}</a>'
        )

    category_display.short_description = 'Категория'

@admin.register(Category)
class CayeloryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_link']

    def image_link(self, category):
        return format_html(
            f'<target="_blank" href={category.image.url}></a>'
            + f'<img src={category.image.url} height="35"'
            +'</a>'
            ) 

    image_link.short_description = 'Изображение'

admin.site.register(Order)