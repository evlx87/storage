import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from backend.product.models import Product


def load_from_json(file_name):
    with open(os.path.join(settings.JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            Product.objects.create(**product)
