from django.urls import path
from backend.product.views import main

app_name = 'product'

urlpatterns = [
    path('', main, name='main'),
]

