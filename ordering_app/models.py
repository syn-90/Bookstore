from django.db import models
from django.conf import settings
from product_app.models import ProductModel
# Create your models here.


class BasketOrderModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateTimeField(null=True, blank=True)
    def sum_basket(self):
        final_price = 0
        try:
            for detail in self.orderdetailmodel_set.all():
                if detail.product.is_off is not None:
                    final_price += detail.final_product_price_with_off()
                else:
                    final_price +=detail.final_product_price()

            return int(final_price)
        except:
            return 0

class OrderDetailModel(models.Model):
    basket = models.ForeignKey(BasketOrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    off = models.FloatField()
    def final_product_price(self):
        res = int(self.product.price  * self.count)
        return round(res)
    def final_product_price_with_off(self):
        res = int(self.product.price - (self.product.price * (self.product.is_off / 100))) * self.count
        return round(res)