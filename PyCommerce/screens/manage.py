from django.http.response import HttpResponse
from django.shortcuts import render
import requests
import json

url = "http://angulardemo.somee.com/Products"

getAllProductsForTable = requests.get(url + "//GetAllProductsForTable")
getAllCategory = requests.get(url + "/GetAllCategory")
getSubCategory = requests.get(url + "/GetSubCategory")
getAllBrands = requests.get(url + "/getAllBrands")

productsTable = [product for product in getAllProductsForTable.json()]
categories = [category for category in getAllCategory.json()]
subCategories = [sub for sub in getSubCategory.json()]
brands = [brand for brand in getAllBrands.json()]

def manage(request):
    return render(request, 'manage/manage.html',
                  {'Categories': categories,
                   'subCategories': subCategories,
                   },)

def manage_products(request):
    return render(request, 'manage/products.html',
                  {'Categories': categories,
                   'subCategories': subCategories,
                   'Products': productsTable
                   },)

def product_edit(request, product_Id):
    if request.method == "POST":
        response = request.POST
        params = {
            "Id": product_Id,
            "NameA": response["NameA"],
            "NameL": response["NameL"],
            "CategoryId": response["CategoryId"],
            "ImageUrl2": response["ImageUrl2"],
            "ImageUrl3": response["ImageUrl3"],
            "ImageUrl7": response["ImageUrl7"],
            "BrandId": response["BrandId"],
            "Description": response["Description"]
        }
        update = requests.post(url + "/updateProduct", params=params)
        print(update.text)
        
    getProduct = requests.get(url + "/getproduct", params={"id": product_Id})
    products = getProduct.text
    products = json.loads(products)

    return render(request, 'manage/edit/product.html', {
        'Categories': categories,
        'subCategories': subCategories,
        'Products': products,
        'Brands': brands
    })
