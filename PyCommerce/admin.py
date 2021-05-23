from .models import brands, cartTransactions, cartTransactionMasters, categories, countries, getHomeProducts, inventoryBalances, inventoryDetails, orderMasters, orderStatus, orders, productSpecifications, productStoreRatings, products, shippingAgents, shippingAgentUsers, shippingDetails, specificationValueCounts, specifications, storeShippingAgents, stores, transactionTypes, users, vendorPriceLists, vendors
from django.contrib import admin


class BrandsAdmin(admin.ModelAdmin):
    list_display = ('id', 'NameA', 'NameL')


class CartTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'ProductId', 'MasterId',
                    'StoreId', 'Quantity', 'IsOrdered')


class CartTransactionMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'DateCreated')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'MainCategoryId',
                    'NameA', 'NameL', 'Level', 'ImageUrl')


class CountriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'NameA', 'NameL', 'Symbol')


class InventoryBalanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'StoreId', 'ProductId', 'QuantityBalance')


class InventoryDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'StoreId', 'ProductId', 'Quantity')


class OrderMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'cartId', 'UserId', 'DateCreated',
                    'ShippingAdress', 'OrderStatusId')


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'Code', 'StatusNameA', 'StatusNameL')


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('ProductId', 'StoreId', 'cartId', 'MasterId', 'UserId', 'Quantity',
                    'ShippingAgentId', 'UnitPrice', 'TotalPrice', 'isDelivered',
                    'DeliveredByUserId', 'Latitude', 'Longitude')


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'NameA', 'NameL', 'CategoryId',
                    'BrandId')


class ProductSpecificationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'CategoryId', 'ProductId', 'SpecificationId',
                    'SpecificationName', 'SpecificationValue', 'ShowInFilter')


class ProductStoreRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'ProductId', 'StoreId', 'UserId',
                    'RatingId', 'ProductReview')


class ShippingAgentAdmin(admin.ModelAdmin):
    list_display = ('NameA', 'NameL', 'Adress1', 'Adress2',
                    'Phone', 'Email', 'Password', 'PostCode')


class ShippingAgentUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'UserId', 'ShippingAgentId')


class ShippingDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ShippingAgentId', 'OrderId', 'DeliveryNotes')


class SpecificationValueCountsAdmin(admin.ModelAdmin):
    list_display = ('SpecificationValue', 'SpecificationCount')


class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'NameA', 'NameL', 'ShowInFilter')


class StoreShippingAgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'StoreId', 'ShippingAgentId')


class StoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'NameA', 'NameL', 'Address', 'VendorId',
                    'CountryId', 'City')


class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'Code', 'NameA', 'NameL')


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'NameA', 'NameL', 'Email', 'Password', 'City')


class VendorPriceListAdmin(admin.ModelAdmin):
    list_display = ('id', 'VendorId', 'ProductId', 'CountryId', 'Price')


class VendorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'NameA', 'NameL', 'Adress1', 'Adress2',
                    'Phone', 'Email', 'Password', 'PostCode')


class GetHomeProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'StoreId', 'ProductId', 'QuantityBalance', 'ProductName',
                    'StoreName', 'ImageUrl', 'ImageUrl6', 'ImageUrl7', 'Description', 'Price',
                    'Currency', 'CategoryId', 'PageNumber')


admin.site.register(brands, BrandsAdmin)
admin.site.register(cartTransactions, CartTransactionAdmin)
admin.site.register(cartTransactionMasters, CartTransactionMasterAdmin)
admin.site.register(categories, CategoryAdmin)
admin.site.register(countries, CountriesAdmin)
admin.site.register(inventoryBalances, InventoryBalanceAdmin)
admin.site.register(inventoryDetails, InventoryDetailAdmin)
admin.site.register(orderMasters, OrderMasterAdmin)
admin.site.register(orderStatus, OrderStatusAdmin)
admin.site.register(orders, OrdersAdmin)
admin.site.register(products, ProductsAdmin)
admin.site.register(productSpecifications, ProductSpecificationsAdmin)
admin.site.register(productStoreRatings, ProductStoreRatingAdmin)
admin.site.register(shippingAgents, ShippingAgentAdmin)
admin.site.register(shippingAgentUsers, ShippingAgentUserAdmin)
admin.site.register(shippingDetails, ShippingDetailsAdmin)
admin.site.register(specificationValueCounts, SpecificationValueCountsAdmin)
admin.site.register(specifications, SpecificationsAdmin)
admin.site.register(storeShippingAgents, StoreShippingAgentAdmin)
admin.site.register(stores, StoresAdmin)
admin.site.register(transactionTypes, TransactionTypeAdmin)
admin.site.register(users, UsersAdmin)
admin.site.register(vendorPriceLists, VendorPriceListAdmin)
admin.site.register(vendors, VendorsAdmin)
admin.site.register(getHomeProducts, GetHomeProductsAdmin)
