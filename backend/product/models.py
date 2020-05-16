from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name='название', max_length=128)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    price = models.DecimalField(verbose_name='цена товара', max_digits=8, decimal_places=0, default=0)
    image = models.ImageField(upload_to='product_images', blank=True, default='no_product_img.png')
