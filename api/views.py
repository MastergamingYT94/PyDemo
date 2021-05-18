from django.shortcuts import render
from PyCommerce.models import Brands
from django.contrib import messages


def InsertBrand(request):
    if request.method == 'POST':
        result = Brands()
        result.NameA = request.POST.get("NameA")
        result.NameL = request.POST.get("NameL")
        result.save()
        return render(request)
