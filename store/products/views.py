from django.shortcuts import render, HttpResponseRedirect
from products.models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required
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


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))










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