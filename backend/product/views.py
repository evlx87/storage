import csv
import mimetypes
import os
from wsgiref.util import FileWrapper

from django.http import HttpResponseRedirect, StreamingHttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from backend.product.forms import ProductForm
from backend.product.models import Product


def main(request):
    context = {
        'page_title': 'Хранилище товаров',
        'stored_products': Product.objects.all()
    }
    return render(request, 'product/index.html', context)


def add_prod(request):
    data = dict()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['list_html'] = render_to_string('product/list.html', {'stored_products': Product.objects.all()})
        else:
            data['form_html'] = render_to_string('product/form.html', {'form': form}, request=request)

    else:
        data['form_is_valid'] = False
        data['form_html'] = render_to_string('product/form.html', {'form': ProductForm()}, request=request)

    return JsonResponse(data)


def file_output(request):
    context = {
        'page_title': 'Подготовка файла CSV',
    }
    return render(request, 'product/output_form.html', context)


def download(request):
    if request.method == 'GET':
        with open('backend/output_files/output.csv', 'w', encoding='utf-8') as file:
            file_writer = csv.writer(file)
            for data in Product.objects.all():
                file_writer.writerow([data.name])
        file.close()

    file_link = 'backend/output_files/output.csv'
    filename = os.path.basename(file_link)

    response = StreamingHttpResponse(FileWrapper(open(file_link, 'rb'), 8192), content_type="text/csv")
    response['Content-Length'] = os.path.getsize(file_link)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
