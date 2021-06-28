from PyCommerce.models import getHomeProducts, categories
from django.core.paginator import Paginator
from django.shortcuts import render
from django import template
import math

HomeProducts = getHomeProducts.objects.all().order_by("StoreId")
getAllCategory = categories.objects.all()
getSubCategory = categories.objects.all()

product_name = [product.ProductName for product in HomeProducts]
Categories = [category for category in getAllCategory]
subCategories = [sub for sub in getSubCategory]


def welcome(request):
    return render(request, 'products/welcome.html', {'Categories': Categories,
                                                     'subCategories': subCategories, })


register = template . Library()


def home(request):
    search = ""
    search_value = ""
    page_number = 1
    if request.method == "POST":
        search_value = request.POST["search"]
    page_number = request.GET.get('page')

    if search_value != "":
        for product in product_name:
            if search_value.lower() in product.lower():
                search = str(product)

    Products = [product for product in HomeProducts]

    paginator = Paginator(Products, 8)
    page = paginator.get_page(page_number)
    products = page.object_list

    maxPageNumber = len(Products) / 8
    maxPageNumber = math.ceil(maxPageNumber)

    return render(request, 'products/home.html',
                  {
                      'Products':  products,
                      'Categories': Categories,
                      'subCategories': subCategories,
                      'Search': search,
                      'MaxPageNumber': range(1, maxPageNumber + 1),
                      'Paginator': page
                  },
                  )
