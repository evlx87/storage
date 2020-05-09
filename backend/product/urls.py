from django.urls import path
import backend.product.views as product_app

app_name = 'product'

urlpatterns = [
    path('', product_app.main, name='index'),
    path('add', product_app.add_product, name='add'),
    path('output', product_app.file_output, name='output'),
    path('download', product_app.download, name='download')
]

