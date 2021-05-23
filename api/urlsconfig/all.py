from django.urls import path
from ..get import all, get, homeProducts

urlpatterns = [
    path('<model>', all.get_all_data),
    path('<model>/<int:id>', get.get_data),
    path('getHomeProducts/page=<int:page>/specValue=<specValue>/search=<search>/category=<int:categoryId>',
         homeProducts.get_home_products),
    path('getMaxPage/specValue=<specValue>/search=<search>/category=<int:categoryId>',
         homeProducts.get_max_page),
    path('productNames/<search>', homeProducts.get_searched_products),
]
