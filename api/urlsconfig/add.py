from django.urls import path
from api.add import deliverOrder, deliveryNotes, user
from ..add import add, cart, cartItem, authUser, order, rateProduct, copyProSpec
<<<<<<< HEAD
from ..update import quantity, update
=======
from ..update import quantity, update, images
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6
from ..delete import deleteCart, deleteItem

urlpatterns = [
    path('cartItem', cartItem.add_cart_item),
    path('updateQuantity/<int:cartId>/<Quantity>',
         quantity.update_cart_quantity),
    path('shoppingCartMaster', cart.add_cart_master),
    path('order/<int:cartId>/<int:userId>', order.add_order),
    path('notes/<int:OrderId>/<int:UserId>', deliveryNotes.add_delivery_notes),
    path('deliverOrder/<int:OrderId>/<int:UserId>', deliverOrder.deliver_order),
<<<<<<< HEAD
=======
    path('updateImages/<int:id>', images.update_images),
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6
    path('rateProduct', rateProduct.rate_product),
    path('copyProSpec/<int:ProductSpecId>/<int:ProductId>/<int:CategoryId>',
         copyProSpec.copy_product_specifications),

    path('authUser', authUser.authenticate_user),
    path('registerUser', user.register_user),

    path('deleteCart/<int:cartId>', deleteCart.delete_cart),
    path('deleteItem/<int:id>', deleteItem.delete_cart_item),
    path('<model>', add.add_data),
    path('<model>/<int:id>', update.update_data),
]
