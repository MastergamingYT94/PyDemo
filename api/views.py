from django.shortcuts import render
from PyCommerce.models import brands
from django.contrib import messages


def InsertBrand(request):
    if request.method == 'POST':
        saveRecord = brands()
        saveRecord.NameA = request.POST.get("NameA")
        saveRecord.NameL = request.POST.get("NameL")
        saveRecord.save()
        return render(request)
    else:
        return render(request)
