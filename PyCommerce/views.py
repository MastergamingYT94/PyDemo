from django.http.response import HttpResponse

# Create your views here.


def welcome(request):
    return HttpResponse('WELCOME TO PYCOMMERCE')
