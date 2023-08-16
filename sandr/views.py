from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .models import *
# Create your views here.
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def index(request):
    products = products_model.objects.all()
    context = {'products_model' : products}
    return render(request , 'index.html',context)
def product_search(request):
    id_or_name = request.GET.get('search')
    if cache.get(id_or_name):
        products = cache.get(id_or_name)
        print('data from cache:')
    else:
        try:
            products = products_model.objects.filter(product_id=id_or_name)
            print('data from DB:')
            cache.set(id_or_name,products)
            
        except:
            products = products_model.objects.filter(products_name__contains=id_or_name)
            print('data from DB:')
            cache.set(id_or_name,products)
    context = {'id':id_or_name , 'x' : products}
    return render(request , 'search.html',context)