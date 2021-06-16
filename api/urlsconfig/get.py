from api.get import get
from django.urls import path
from api.get.items import assignCategory, cartItem, checkProduct, loginAsGuest, productRating, user, orders, ordersShipping, ordersMaster, shippingDetails

urlpatterns = [
    path('assignCategory/<int:MainCategory>',
         assignCategory.assign_categories),
    #     path('productRate/<int:ProductId>', productRating.get_product_rating),
    path('cartItem/<int:ProductId>', cartItem.get_cart_item),
    path('user/<int:UserId>', user.get_user),
    path('checkProduct/<int:StoreId>/<int:ProductId>',
         checkProduct.check_product_exists),
    path('loginAsGuest', loginAsGuest.login_as_guest),

    path('orders/<userId>', orders.get_orders),
    path('ordersMaster/<int:UserId>', ordersMaster.get_orders_master),
    path('ordersShipping/<int:UserId>', ordersShipping.get_orders_shipping),
    path('shippingDetails/<int:UserId>', shippingDetails.get_shipping_details),

    path('<model>/<id>', get.get_data)
]
