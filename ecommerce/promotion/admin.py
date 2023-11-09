from django.contrib import admin
from . import models
from .tasks import promotion_prices

class ProductOnPromotion(admin.StackedInline):
    model = models.Promotion.products_on_promotion.through
    extra = 4

class ProductInventoryList(admin.ModelAdmin):
    model = models.Promotion
    inlines = (ProductOnPromotion,)
    list_display = ('name', 'is_active', 'promo_start', 'promo_end')

    def save_model(self, request, promotion, form, change):
        super().save_model(request, promotion, form, change)
        promotion_prices.delay(promotion.promo_reduction, promotion.id)

admin.site.register(models.Promotion, ProductInventoryList)
admin.site.register(models.PromoType)
admin.site.register(models.Coupon)
