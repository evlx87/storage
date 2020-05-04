from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name='название', max_length=128)
    date = models.DateField(verbose_name='дату поступления')
    quantity = models.DecimalField(verbose_name='количество', max_digits=4, decimal_places=0, default=1)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=0, default=0)
    provider = models.CharField(verbose_name='имя поставщика', max_length=256, blank=True)
