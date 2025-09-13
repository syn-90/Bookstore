from django.db import models
from product_app.models import ProductModel
# Create your models here.
from Config import settings


class FavoriteProductsModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)