from django.shortcuts import render
from PyCommerce.models import brands
from django.contrib import messages


def InsertBrand(request):
    if request.method == 'POST':
        result = brands()
        result.NameA = request.POST.get("NameA")
        result.NameL = request.POST.get("NameL")
        result.save()
        return render(request)
