from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "products/index.html")


def products(request):
    return render(request, "products/products.html")


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