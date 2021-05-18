from django.urls import path
from ..get.all import brands, cartTransactions, cartTransactionMasters, categories, countries, inventoryBalances, inventoryDetails, orderMasters, orderStatus, orders, products, productSpecifications, productStoreRatings, shippingAgents, shippingAgentUsers, shippingDetails, specifications, specificationValueCounts, stores, storeShippingAgents, transactionTypes, users, vendorPriceLists, vendors, homeProducts


urlpatterns = [
    path('brands', brands.get_brands),
    path('cartTransaction', cartTransactions.get_cart_transactions),
    path('cartTransactionMaster',
         cartTransactionMasters.get_cart_transaction_masters),
    path('categories', categories.get_categories),
    path('countries', countries.get_countries),
    path('inventoryBalance', inventoryBalances.get_inventory_balances),
    path('inventoryDetail', inventoryDetails.get_inventory_details),
    path('orderMaster', orderMasters.get_order_masters),
    path('orderStatus', orderStatus.get_order_status),
    path('orders', orders.get_orders),
    path('products', products.get_products),
    path('productSpecifications', productSpecifications.get_product_specifications),
    path('productStoreRating', productStoreRatings.get_product_store_ratings),
    path('shippingAgents', shippingAgents.get_shipping_agents),
    path('shippingAgentUsers', shippingAgentUsers.get_shipping_agent_users),
    path('shippingDetails', shippingDetails.get_shipping_details),
    path('specificationValueCounts',
         specificationValueCounts.get_specification_value_counts),
    path('specifications', specifications.get_specifications),
    path('storeShippingAgents', storeShippingAgents.get_store_shipping_agents),
    path('stores', stores.get_stores),
    path('transactionType', transactionTypes.get_transaction_types),
    path('users', users.get_users),
    path('vendorPriceList', vendorPriceLists.get_vendor_price_lists),
    path('vendors', vendors.get_vendors),

    path('getHomeProducts/page=<int:page>/specValue=<specValue>/search=<search>/category=<int:categoryId>',
         homeProducts.get_home_products),
    path('getMaxPage/specValue=<specValue>/search=<search>/category=<int:categoryId>',
         homeProducts.get_max_page),
    path('productNames/<search>', homeProducts.get_searched_products),
]
