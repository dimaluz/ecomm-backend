from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ecommerce.inventory import models
from ecommerce.drf.serializer import CategorySerializer, ProductSerializer, ProductInventorySerializer

class CategoryList(APIView):
    #Return a list of all categories
    def get(self, request):
        queryset = models.Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductByCategory(APIView):
    #Return product by category
    def get(self, request, query=None):
        queryset = models.Product.objects.filter(category__slug=query)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    

class ProductInventoryByWebId(APIView):
    #Return sub-product by webId
    def get(self, request, query=None):
        queryset = models.ProductInventory.objects.filter(product__web_id=query)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)