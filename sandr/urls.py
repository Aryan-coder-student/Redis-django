from django.urls import path
from .views import *
urlpatterns = [
    path('' , index , name = 'index'),
    path('product', product_search , name = 'product_search'),
    # path('/?search', product_search , name = 'product_search'),
]
