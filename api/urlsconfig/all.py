from django.urls import path
from ..get import all, get
from ..get.items import homeProducts, specifications, subCategories, mainCategories, reviews, proSpecInv, cart, ordersFiltered

urlpatterns = [
    path('mainCategories', mainCategories.get_main_categories),
    path('subCategories', subCategories.get_sub_categories),
    path('cart/<CartId>', cart.get_cart_item),
    path('proSpecInv/<int:ProductId>',
         proSpecInv.get_product_specifications_inv),
    path('spec/<CategoryId>', specifications.get_specifications),
    path('reviews/<int:ProductId>', reviews.get_reviews),
    path('reviews/', reviews.get_reviews),
    path('ordersFiltered/<int:UserId>/<int:Status>',
         ordersFiltered.get_orders_filtered),

    path('getHomeProducts/page=<int:page>/specValue=<specValue>/search=<search>/category=<int:categoryId>',
         homeProducts.get_home_products),
    path('getMaxPage/specValue=<specValue>/search=<search>/category=<int:categoryId>',
         homeProducts.get_max_page),
    path('productNames/<search>', homeProducts.get_searched_products),
    path('productNames/', homeProducts.get_searched_products),

    path('<model>', all.get_all_data),
    path('<model>/<int:id>', get.get_data),
]
