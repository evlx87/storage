from django.shortcuts import render
from backend.product.models import Product


def main(request):
    context = {
        'page_title': 'Хранилище товаров',
        'stored_products': Product.objects.all()
    }
    return render(request, 'index.html', context)

