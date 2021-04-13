from PyCommerce.models import brands, cartTransaction, cartTransactionMaster, category, countries, inventoryBalance, inventoryDetail, orderMaster, orderStatus, orders, productSpecifications, productStoreRating, products, shippingAgent, shippingAgentUser, shippingDetails, specificationValueCounts, specifications, storeShippingAgent, stores, transactionType, users, vendorPriceList, vendors, getHomeProducts
from rest_framework import serializers
import math


class BrandsResource(serializers.ModelSerializer):
    class Meta:
        model = brands
        fields = ['Id', 'NameA', 'NameL']


class CartTransactionResource(serializers.ModelSerializer):
    class Meta:
        model = cartTransaction
        fields = ['Id', 'ProductId', 'MasterId',
                  'StoreId', 'Quantity', 'IsOrdered']


class CartTransactionMasterResource(serializers.ModelSerializer):
    class Meta:
        model = cartTransactionMaster
        fields = ['Id', 'DateCreated']


class CategoryResource(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['Id', 'MainCategoryId',
                  'NameA', 'NameL', 'Level', 'ImageUrl']


class CountriesResource(serializers.ModelSerializer):
    class Meta:
        model = countries
        fields = ['Id', 'NameA', 'NameL', 'Symbol']


class InventoryBalanceResource(serializers.ModelSerializer):
    class Meta:
        model = inventoryBalance
        fields = ['Id', 'StoreId', 'ProductId', 'QuantityBalance']


class InventoryDetailResource(serializers.ModelSerializer):
    class Meta:
        model = inventoryDetail
        fields = ['Id', 'TransType', 'TransDate',
                  'StoreId', 'ProductId', 'Quantity']


class OrderMasterResource(serializers.ModelSerializer):
    class Meta:
        model = orderMaster
        fields = ['Id', 'cartId', 'UserId', 'DateCreated',
                  'ShippingAdress', 'OrderStatusId']


class OrderStatusResource(serializers.ModelSerializer):
    class Meta:
        model = orderStatus
        fields = ['Id', 'Code', 'StatusNameA', 'StatusNameL']


class OrdersResource(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = ['ProductId', 'StoreId', 'cartId', 'MasterId', 'UserId', 'Quantity',
                  'ShippingAgentId', 'UnitPrice', 'TotalPrice', 'isDelivered', 'MapLocation',
                  'DeliveredByUserId', 'Latitude', 'Longitude']


class ProductsResource(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ['Id', 'NameA', 'NameL', 'ImageUrl', 'ImageUrl6',
                  'ImageUrl7', 'CategoryId', 'BrandId', 'Description']


class ProductSpecificationsResource(serializers.ModelSerializer):
    class Meta:
        model = productSpecifications
        fields = ['Id', 'CategoryId', 'ProductId', 'SpecificationId',
                  'SpecificationName', 'SpecificationValue', 'ShowInFilter']


class ProductStoreRatingResource(serializers.ModelSerializer):
    class Meta:
        model = productStoreRating
        fields = ['Id', 'ProductId', 'StoreId', 'UserId',
                  'RatingId', 'ProductReview']


class ShippingAgentResource(serializers.ModelSerializer):
    class Meta:
        model = shippingAgent
        fields = ['Id', 'NameA', 'NameL', 'Adress1', 'Adress2',
                  'Phone', 'Email', 'Password', 'PostCode']


class ShippingAgentUserResource(serializers.ModelSerializer):
    class Meta:
        model = shippingAgentUser
        fields = ['Id', 'UserId', 'ShippingAgentId']


class ShippingDetailsResource(serializers.ModelSerializer):
    class Meta:
        model = shippingDetails
        fields = ['Id', 'ShippingAgentId', 'OrderId', 'DeliveryNotes']


class SpecificationValueCountsResource(serializers.ModelSerializer):
    class Meta:
        model = specificationValueCounts
        fields = ['SpecificationValue', 'SpecificationCount']


class SpecificationsResource(serializers.ModelSerializer):
    class Meta:
        model = specifications
        fields = ['Id', 'NameA', 'NameL', 'ShowInFilter']


class StoreShippingAgentResource(serializers.ModelSerializer):
    class Meta:
        model = storeShippingAgent
        fields = ['Id', 'StoreId', 'ShippingAgentId']


class StoresResource(serializers.ModelSerializer):
    class Meta:
        model = stores
        fields = ['Id', 'VendorId', 'NameA', 'NameL', 'email', 'Address',
                  'CountryId', 'City', 'MapLocation', 'ShippingAgentId']


class TransactionTypeResource(serializers.ModelSerializer):
    class Meta:
        model = transactionType
        fields = ['Id', 'Code', 'NameA', 'NameL']


class UsersResource(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['Id', 'NameA', 'NameL', 'Email', 'Password', 'City']


class VendorPriceListResource(serializers.ModelSerializer):
    class Meta:
        model = vendorPriceList
        fields = ['Id', 'VendorId', 'ProductId', 'CountryId', 'Price']


class VendorsResource(serializers.ModelSerializer):
    class Meta:
        model = vendors
        fields = ['Id', 'NameA', 'NameL', 'Adress1', 'Adress2',
                  'Phone', 'Email', 'Password', 'PostCode']


class GetHomeProductsResource(serializers.ModelSerializer):
    class Meta:
        model = getHomeProducts
        fields = ['Id', 'StoreId', 'ProductId', 'QuantityBalance', 'ProductName',
                  'StoreName', 'ImageUrl', 'ImageUrl6', 'ImageUrl7', 'Description', 'Price',
                  'Currency', 'CategoryId', 'PageNumber', 'FiveStarsCount', 'FourStarsCount',
                  'ThreeStarsCount', 'TwoStarsCount', 'OneStarsCount', 'MaxTotalRating', 'finalProductRating', 'OutOfFivestring']
