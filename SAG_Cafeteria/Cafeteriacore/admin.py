from django.contrib import admin
from .models import ExtendedUserInfo, Item, Order, StockStatus


class ExtendedUserInfoAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


class StockStatusAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExtendedUserInfo, ExtendedUserInfoAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(StockStatus, StockStatusAdmin)
