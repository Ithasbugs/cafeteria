from django.db import models
from django.contrib.auth.models import User


class ExtendedUserInfo(models.Model):
    user = models.OneToOneField(User, related_name='extended_info',
                                on_delete=models.CASCADE)
    phone_number = models.CharField(null=True, blank=True, max_length=15)
    employee_id = models.CharField(null=True, blank=True, max_length=250)
    organization = models.CharField(null=True, blank=True, max_length=250)
    id_card = models.ImageField(upload_to='', null=True, blank=True)


class Item(models.Model):
    item_name = models.CharField(null=True, blank=True, max_length=250)
    price = models.FloatField()


class StockStatus(models.Model):
    item = models.OneToOneField(Item, related_name='item',
                                on_delete=models.CASCADE)
    total_items = models.IntegerField(null=True, blank=True)
    ordered_count = models.IntegerField(null=True, blank=True)


class Order(models.Model):
    items = models.ForeignKey(Item, related_name='items',
                              on_delete=models.CASCADE)
    customer = models.OneToOneField(User, related_name='customer',
                                    on_delete=models.CASCADE)
    order_status = models.BooleanField(default=False)
    order_id = models.IntegerField()
