import csv

from django.http import HttpResponseRedirect
from django.shortcuts import render

from backend.product.forms import ProductForm
from backend.product.models import Product


def main(request):
    context = {
        'page_title': 'Хранилище товаров',
        'stored_products': Product.objects.all()
    }
    return render(request, 'index.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()

    context = {
        'page_title': 'Добавление нового товара',
        'form': form
    }
    return render(request, 'add_product.html', context)


def file_output(request):
    context = {
        'page_title': 'Подготовка файла CSV',
    }
    return render(request, 'output_form.html', context)
