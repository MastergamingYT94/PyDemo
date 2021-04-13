from PyCommerce.models import getHomeProducts
from django.core.paginator import Paginator
from django.shortcuts import render
import math

import requests
url = "http://angulardemo.somee.com/Products"


HomeProducts = getHomeProducts.objects.all().order_by("StoreId")
getAllCategory = requests.get(url + "/GetAllCategory")
getSubCategory = requests.get(url + "/GetSubCategory")

product_name = [product.ProductName for product in HomeProducts]
categories = [category for category in getAllCategory.json()]
subCategories = [sub for sub in getSubCategory.json()]


def welcome(request):
    return render(request, 'products/welcome.html', {'Categories': categories,
                                                     'subCategories': subCategories, })


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
                  {'Products':  products,
                   'Categories': categories,
                   'subCategories': subCategories,
                   'Search': search,
                   'MaxPageNumber': range(1, maxPageNumber + 1),
                   'Paginator': page
                   },
                  )
