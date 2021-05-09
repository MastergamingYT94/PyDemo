from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('all/', include('api.urlsconfig.all')),
    path('get/', include('api.urlsconfig.get')),
    path('add/', include('api.urlsconfig.add')),

]
