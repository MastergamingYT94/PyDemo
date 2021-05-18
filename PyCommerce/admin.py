from .models import Brands, CartTransactions, CartTransactionMasters, Categories, Countries, InventoryBalances, InventoryDetails, OrderMasters, OrderStatus, Orders, ProductSpecifications, ProductStoreRatings, Products, ShippingAgents, ShippingAgentUsers, ShippingDetails, SpecificationValueCounts, Specifications, StoreShippingAgents, Stores, TransactionTypes, Users, VendorPriceLists, Vendors, GetHomeProducts
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


admin.site.register(Brands, BrandsAdmin)
admin.site.register(CartTransactions, CartTransactionAdmin)
admin.site.register(CartTransactionMasters, CartTransactionMasterAdmin)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(InventoryBalances, InventoryBalanceAdmin)
admin.site.register(InventoryDetails, InventoryDetailAdmin)
admin.site.register(OrderMasters, OrderMasterAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductSpecifications, ProductSpecificationsAdmin)
admin.site.register(ProductStoreRatings, ProductStoreRatingAdmin)
admin.site.register(ShippingAgents, ShippingAgentAdmin)
admin.site.register(ShippingAgentUsers, ShippingAgentUserAdmin)
admin.site.register(ShippingDetails, ShippingDetailsAdmin)
admin.site.register(SpecificationValueCounts, SpecificationValueCountsAdmin)
admin.site.register(Specifications, SpecificationsAdmin)
admin.site.register(StoreShippingAgents, StoreShippingAgentAdmin)
admin.site.register(Stores, StoresAdmin)
admin.site.register(TransactionTypes, TransactionTypeAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(VendorPriceLists, VendorPriceListAdmin)
admin.site.register(Vendors, VendorsAdmin)
admin.site.register(GetHomeProducts, GetHomeProductsAdmin)
