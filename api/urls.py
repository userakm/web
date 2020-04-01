from django.urls import path
from api.views import product_list, products_detail, category_list, category_detail, category_product

urlpatterns = [
    path('products/', product_list),
    path('products/<int:id>/', products_detail),
    path('categories/', category_list),
    path('categories/<int:id>/', category_detail),
    path('categories/<int:id>/products', category_product),
]