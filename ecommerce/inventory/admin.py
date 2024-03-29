from django.contrib import admin
from . import models

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Brand)
admin.site.register(models.Media)
admin.site.register(models.ProductAttribute)
admin.site.register(models.ProductType)
admin.site.register(models.Stock)
admin.site.register(models.ProductAttributeValue)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'store_price')

admin.site.register(models.ProductInventory, InventoryAdmin)