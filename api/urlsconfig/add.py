from django.db import router
from django.urls import path
from api.add import deliverOrder, deliveryNotes, user
from ..add import add, cart, cartItem, authUser, order, rateProduct, copyProSpec, product
from ..update import quantity, update, updateUser, updateProduct
from ..delete import deleteCart, deleteItem

urlpatterns = [
    path('cartItem', cartItem.add_cart_item),
    path('updateQuantity/<int:cartId>/<Quantity>',
         quantity.update_cart_quantity),
    path('shoppingCartMaster', cart.add_cart_master),
    path('order/<int:cartId>/<int:userId>', order.add_order),
    path('notes/<int:OrderId>/<int:UserId>', deliveryNotes.add_delivery_notes),
    path('deliverOrder/<int:OrderId>/<int:UserId>', deliverOrder.deliver_order),
    path('rateProduct', rateProduct.rate_product),
    path('copyProSpec/<int:ProductSpecId>/<int:ProductId>/<int:CategoryId>',
         copyProSpec.copy_product_specifications),
    path('addProduct', product.add_product),

    path('authUser', authUser.authenticate_user),
    path('registerUser', user.register_user),
    path('updateUser/<int:id>', updateUser.update_user),
    path('updateProduct/<int:id>', updateProduct.update_product),

    path('deleteCart/<int:cartId>', deleteCart.delete_cart),
    path('deleteItem/<int:id>', deleteItem.delete_cart_item),
    path('<model>', add.add_data),
    path('<model>/<int:id>', update.update_data),
]
