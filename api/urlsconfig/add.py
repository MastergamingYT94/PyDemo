from django.urls import path
from ..add import brand, category, product, shippingAgent, shippingAgnetUser, store, vendor, vendorPriceList

urlpatterns = [
    path('brand', brand.add_brand),
    path('category', category.add_category),
    path('product', product.add_product),
    path('shippingAgent', shippingAgent.add_shipping_agent),
    path('shippingAgentUser', shippingAgnetUser.add_shipping_agent_user),
    path('store', store.add_store),
    path('vendor', vendor.add_vendor),
    path('vendorPriceList', vendorPriceList.add_price_list),
]
