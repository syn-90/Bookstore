from django.db import models
from django.conf import settings
from product_app.models import ProductModel
# Create your models here.


class BasketOrderModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(null=True, blank=True)

class OrderDetailModel(models.Model):
    basket = models.ForeignKey(BasketOrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    off = models.FloatField()