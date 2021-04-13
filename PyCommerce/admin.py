from .models import brands, cartTransaction, cartTransactionMaster, category, countries, inventoryBalance, inventoryDetail, orderMaster, orderStatus, orders, productSpecifications, productStoreRating, products, shippingAgent, shippingAgentUser, shippingDetails, specificationValueCounts, specifications, storeShippingAgent, stores, transactionType, users, vendorPriceList, vendors, getHomeProducts
from django.contrib import admin


class BrandsAdmin(admin.ModelAdmin):
    list_display = ('Id', 'NameA', 'NameL')


class CartTransactionAdmin(admin.ModelAdmin):
    list_display = ('Id', 'ProductId', 'MasterId',
                    'StoreId', 'Quantity', 'IsOrdered')


class CartTransactionMasterAdmin(admin.ModelAdmin):
    list_display = ('Id', 'DateCreated')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Id', 'MainCategoryId',
                    'NameA', 'NameL', 'Level', 'ImageUrl')


class CountriesAdmin(admin.ModelAdmin):
    list_display = ('Id', 'NameA', 'NameL', 'Symbol')


class InventoryBalanceAdmin(admin.ModelAdmin):
    list_display = ('Id', 'StoreId', 'ProductId', 'QuantityBalance')


class InventoryDetailAdmin(admin.ModelAdmin):
    list_display = ('Id', 'TransType', 'TransDate',
                    'StoreId', 'ProductId', 'Quantity')


class OrderMasterAdmin(admin.ModelAdmin):
    list_display = ('Id', 'cartId', 'UserId', 'DateCreated',
                    'ShippingAdress', 'OrderStatusId')


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Code', 'StatusNameA', 'StatusNameL')


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('ProductId', 'StoreId', 'cartId', 'MasterId', 'UserId', 'Quantity',
                    'ShippingAgentId', 'UnitPrice', 'TotalPrice', 'isDelivered', 'MapLocation',
                    'DeliveredByUserId', 'Latitude', 'Longitude')


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('Id', 'NameA', 'NameL', 'CategoryId',
                    'BrandId')


class ProductSpecificationsAdmin(admin.ModelAdmin):
    list_display = ('Id', 'CategoryId', 'ProductId', 'SpecificationId',
                    'SpecificationName', 'SpecificationValue', 'ShowInFilter')


class ProductStoreRatingAdmin(admin.ModelAdmin):
    list_display = ('Id', 'ProductId', 'StoreId', 'UserId',
                    'RatingId', 'ProductReview')


class ShippingAgentAdmin(admin.ModelAdmin):
    list_display = ('Id', 'NameA', 'NameL', 'Adress1', 'Adress2',
                    'Phone', 'Email', 'Password', 'PostCode')


class ShippingAgentUserAdmin(admin.ModelAdmin):
    list_display = ('Id', 'UserId', 'ShippingAgentId')


class ShippingDetailsAdmin(admin.ModelAdmin):
    list_display = ('Id', 'ShippingAgentId', 'OrderId', 'DeliveryNotes')


class SpecificationValueCountsAdmin(admin.ModelAdmin):
    list_display = ('SpecificationValue', 'SpecificationCount')


class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ('Id', 'NameA', 'NameL', 'ShowInFilter')


class StoreShippingAgentAdmin(admin.ModelAdmin):
    list_display = ('Id', 'StoreId', 'ShippingAgentId')


class StoresAdmin(admin.ModelAdmin):
    list_display = ('Id', 'VendorId', 'NameA', 'NameL', 'email', 'Address',
                    'CountryId', 'City', 'MapLocation', 'ShippingAgentId')


class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Code', 'NameA', 'NameL')


class UsersAdmin(admin.ModelAdmin):
    list_display = ('Id', 'NameA', 'NameL', 'Email', 'Password', 'City')


class VendorPriceListAdmin(admin.ModelAdmin):
    list_display = ('Id', 'VendorId', 'ProductId', 'CountryId', 'Price')


class VendorsAdmin(admin.ModelAdmin):
    list_display = ('Id', 'NameA', 'NameL', 'Adress1', 'Adress2',
                    'Phone', 'Email', 'Password', 'PostCode')


class GetHomeProductsAdmin(admin.ModelAdmin):
    list_display = ('Id', 'StoreId', 'ProductId', 'QuantityBalance', 'ProductName',
                    'StoreName', 'ImageUrl', 'ImageUrl6', 'ImageUrl7', 'Description', 'Price',
                    'Currency', 'CategoryId', 'PageNumber')


admin.site.register(brands, BrandsAdmin)
admin.site.register(cartTransaction, CartTransactionAdmin)
admin.site.register(cartTransactionMaster, CartTransactionMasterAdmin)
admin.site.register(category, CategoryAdmin)
admin.site.register(countries, CountriesAdmin)
admin.site.register(inventoryBalance, InventoryBalanceAdmin)
admin.site.register(inventoryDetail, InventoryDetailAdmin)
admin.site.register(orderMaster, OrderMasterAdmin)
admin.site.register(orderStatus, OrderStatusAdmin)
admin.site.register(orders, OrdersAdmin)
admin.site.register(products, ProductsAdmin)
admin.site.register(productSpecifications, ProductSpecificationsAdmin)
admin.site.register(productStoreRating, ProductStoreRatingAdmin)
admin.site.register(shippingAgent, ShippingAgentAdmin)
admin.site.register(shippingAgentUser, ShippingAgentUserAdmin)
admin.site.register(shippingDetails, ShippingDetailsAdmin)
admin.site.register(specificationValueCounts, SpecificationValueCountsAdmin)
admin.site.register(specifications, SpecificationsAdmin)
admin.site.register(storeShippingAgent, StoreShippingAgentAdmin)
admin.site.register(stores, StoresAdmin)
admin.site.register(transactionType, TransactionTypeAdmin)
admin.site.register(users, UsersAdmin)
admin.site.register(vendorPriceList, VendorPriceListAdmin)
admin.site.register(vendors, VendorsAdmin)
admin.site.register(getHomeProducts, GetHomeProductsAdmin)
