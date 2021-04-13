from api.get import brand, category, order, product, store, user, vendor
from django.urls import path


urlpatterns = [
    path('brand/<id>', brand.get_brand),
    path('category/<id>', category.get_category),
    path('order/<id>', order.get_order),
    path('product/<id>', product.get_product),
    path('store/<id>', store.get_store),
    path('user/<id>', user.get_user),
    path('vendor/<id>', vendor.get_vendor),
]
