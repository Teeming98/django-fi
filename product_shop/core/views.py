from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest, Http404
from django.urls import reverse
from .models import Product, Category, Order
from django.db.models import Q
from .forms import OrderForm
from datetime import datetime
from random import choice


def index_view(request: HttpRequest):
    return render(request, 'core/index.html', {
        'title': 'Главная страница'
    })

def products_view(request: HttpResponse):

    if request.method == 'GET':
        category_name = request.GET.get('category')
        order_by = request.GET.get('order_by')

        products = Product.objects.all()

        category = None
        if category_name is not None and category_name.strip() != '':
            category = Category.objects.filter(name__icontains = category_name).first()
            
            if category is None:
                products = products.filter(~Q(name__icontains=''))
            else:
                products = products.filter(category = category)

        if order_by is not None:
            products = products.order_by(order_by)

        return render(
            request, 'core/products.html',
            {
                'title': 'Товары',
               'products': products
            }
            )

    return HttpResponse(status = 405)

def get_product(id: int):
    try:
        return Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404
         
def product_view(request: HttpResponse, id: int):
    product = get_product(id)

    if request.method == 'GET':
        if product.category is None:
            pass

        return render(request, 'core/product.html',{
            'title': product.name,
            'product': product
            })       

    return HttpResponse(status = 204)

def make_order_view(request: HttpRequest, product_id: int):
    data = {
        'title': 'Оформление заказа',
        'form': OrderForm(),
        'product': get_product(product_id)
    }

    if request.method == 'GET':
        return render (request, 'core/make_order.html', data)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if not form.is_valid():
            data['error'] = 'Данные заполнены неверно'
            data['form'] = form
            return redirect(reverse('product', kwargs={'id': product_id}))

        try:
            now = datetime.now()
            order = form.save(commit=False)
            order.product = get_product(product_id)
            order.rt = f'{now.date()} {now.time()}'
            order.save()
            return redirect(reverse('products'))
        except Exception as e:
            data['error'] = 'Ошибка при сохранению заказа'
            return redirect(reverse('product', kwargs={'id': product_id}))            

    return HttpResponse(statuc=405)

def cow_view(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'core/cow.html', {'title': 'Корова'})
    
def govz_view(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'core/govz.html', {'tirle': 'Говзич'})

def rand(request: HttpRequest):
    if request.method == 'GET':
        l = ['Да', 'Нет']
        lr = choice(l)

        return render(request, 'core/rand.html', {'title': 'Рандом', 'res': lr})   