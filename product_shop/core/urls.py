from django.urls import path
from.views import *

products_urlpatterns = [
    path('<int:id>/', product_view, name = 'product'),
    path('', products_view, name = 'products'),
    path('<int:product_id>/buy/', make_order_view, name = 'make_order'),
    path('cow/', cow_view, name='cow_view'),   
    path('govz/', govz_view, name='govz_view')   
]

base_urlpatterns = [
    path('', index_view, name = 'home')
]
