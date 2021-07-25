from api.get import get
from django.urls import path
<<<<<<< HEAD
from api.get.items import productRating, assignCategory, cartItem, checkProduct, loginAsGuest, user, orders, ordersShipping, ordersMaster, shippingDetails
=======
from api.get.items import assignCategory, cartItem, checkProduct, loginAsGuest, productRating, user, orders, ordersShipping, ordersMaster, shippingDetails
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6

urlpatterns = [
    path('assignCategory/<int:MainCategory>',
         assignCategory.assign_categories),
    path('productRate/<int:ProductId>', productRating.get_product_rating),
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
