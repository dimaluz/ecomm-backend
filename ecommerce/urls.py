from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ecommerce.drf import views
from ecommerce.search.views import SearchProductInventory


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/inventory/category/all/', views.CategoryList.as_view()),
    path('api/inventory/products/category/<str:query>/', views.ProductByCategory.as_view()),
    path('api/inventory/<int:query>/', views.ProductInventoryByWebId.as_view()),
    path('api/search/<str:query>/', SearchProductInventory.as_view()),
]
