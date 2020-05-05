from django.urls import path
import backend.product.views as product_app

app_name = 'product'

urlpatterns = [
    path('', product_app.main, name='index'),
]

