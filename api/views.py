from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import Http404
from api.models import Product
from api.models import Category


def product_list(request):
    p_list = Product.objects.all()
    products_json = [product.to_json() for product in p_list]
    return JsonResponse(products_json, safe=False)


def products_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(product.to_json())


def category_list(request):
    c_list = Category.objects.all()
    categories_json = [category.to_json() for category in c_list]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(category.to_json())


def category_product(request, id):
    category = Category.objects.get(id=id)
    products = category.product_set.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)