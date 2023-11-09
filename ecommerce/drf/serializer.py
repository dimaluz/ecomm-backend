from rest_framework import serializers
from ecommerce.inventory import models
from ecommerce.promotion.models import Promotion
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ["name", "slug", "is_active"]
        read_only = True

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ["name", "web_id"]
        read_only = True
        editable = False
        
class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Brand
        fields = ["name"]
        read_only = True

class ProductMediaSerializer(serializers.ModelSerializer):

    img_url = serializers.SerializerMethodField()

    class Meta:
        model = models.Media
        fields = ["img_url", "alt_text"]
        read_only = True
        editable = False

    def get_img_url(self, obj):
        return obj.img_url.url
    
class ProductAttributeValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductAttributeValue
        depth = 2
        exclude = ["id"]
        read_only = True

class ProductInventorySerializer(serializers.ModelSerializer):

    brand = BrandSerializer(read_only=True)
    product = ProductSerializer(many=False, read_only=True)
    media = ProductMediaSerializer(many=True, read_only=True)
    attributes = ProductAttributeValueSerializer(
        source="attribute_values",
        many=True,
        read_only=True,
    )
    promotion_price = serializers.SerializerMethodField()

    class Meta:
        model = models.ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "brand",
            "product",
            "is_on_sale",
            "weight",
            "media",
            "attributes",
            "product_type",
            "promotion_price",
        ]
        read_only = True
    
    def get_promotion_price(self, obj):
        try:
            data = Promotion.products_on_promotion.through.objects.get(
                Q(promotion_id__is_active=True) & Q(product_inventory_id=obj.id)
            )
            return data.promo_price
        except ObjectDoesNotExist:
            return None

class ProductInventorySearchSerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=False, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = models.ProductInventory
        fields = [
            'id',
            'sku',
            'store_price',
            'is_default',
            'product',
            'brand',
        ]