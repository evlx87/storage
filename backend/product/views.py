from django.shortcuts import render
from backend.product.models import Product


def main(request):
    return render(request, 'index.html', {'products': Product.objects.all()})

