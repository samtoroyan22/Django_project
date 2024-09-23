from django.shortcuts import render
from products.models import ProductCategory, Product
# Create your views here.


def index(request):
    context = {
        "title": "store",
    }
    return render(request, "products/index.html", context)


def products(request):
    context = {
        "title": "каталог",
        "categories": ProductCategory.objects.all(),
        "products": Product.objects.all(),
    }
    return render(request, "products/products.html", context)


def test_context(request):

    context = {
        "title": "store",
        "header": "hello world",
        "products": [
            {"name": "product-1", "price": 2000},
            {"name": "product-2", "price": 5000},
            {"name": "product-3", "price": 10000},
        ],
        "sale_products": ["product-4", "product-5"]
    }

    return render(request, "products/test_context.html", context)