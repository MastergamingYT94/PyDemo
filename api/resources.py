from api.get.items.storeItems import vendorName, shippingAgentName
from PyCommerce.models import Brands, CartTransactions, CartTransactionMasters, Categories, Countries, InventoryBalances, InventoryDetails, OrderMasters, OrderStatus, Orders, ProductSpecifications, ProductStoreRatings, Products, ShippingAgents, ShippingAgentUsers, ShippingDetails, SpecificationValueCounts, Specifications, StoreShippingAgents, Stores, TransactionTypes, Users, VendorPriceLists, Vendors, GetHomeProducts
from rest_framework import serializers


class brandsResource(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = ['Id', 'NameA', 'NameL']


class cartTransactionsResource(serializers.ModelSerializer):
    class Meta:
        model = CartTransactions
        fields = ['Id', 'ProductId', 'MasterId',
                  'StoreId', 'Quantity', 'IsOrdered']


class cartTransactionMastersResource(serializers.ModelSerializer):
    class Meta:
        model = CartTransactionMasters
        fields = ['Id', 'DateCreated']


class categoriesResource(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['Id', 'MainCategoryId',
                  'NameA', 'NameL', 'Level', 'ImageUrl']


class countriesResource(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['Id', 'NameA', 'NameL', 'Symbol']


class inventoryBalancesResource(serializers.ModelSerializer):
    class Meta:
        model = InventoryBalances
        fields = ['Id', 'StoreId', 'ProductId', 'QuantityBalance']


class inventoryDetailsResource(serializers.ModelSerializer):
    class Meta:
        model = InventoryDetails
        fields = ['Id', 'TransType', 'TransDate',
                  'StoreId', 'ProductId', 'Quantity']


class orderMastersResource(serializers.ModelSerializer):
    class Meta:
        model = OrderMasters
        fields = ['Id', 'cartId', 'UserId', 'DateCreated',
                  'ShippingAdress', 'OrderStatusId']


class orderStatusResource(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['Id', 'Code', 'StatusNameA', 'StatusNameL']


class ordersResource(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['ProductId', 'StoreId', 'cartId', 'MasterId', 'UserId', 'Quantity',
                  'ShippingAgentId', 'UnitPrice', 'TotalPrice', 'isDelivered', 'MapLocation',
                  'DeliveredByUserId', 'Latitude', 'Longitude']


class productsResource(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['Id', 'NameA', 'NameL', 'ImageUrl', 'ImageUrl6',
                  'ImageUrl7', 'CategoryId', 'BrandId', 'Description']


class productSpecificationsResource(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecifications
        fields = ['Id', 'CategoryId', 'ProductId', 'SpecificationId',
                  'SpecificationName', 'SpecificationValue', 'ShowInFilter']


class productStoreRatingsResource(serializers.ModelSerializer):
    class Meta:
        model = ProductStoreRatings
        fields = ['Id', 'ProductId', 'StoreId', 'UserId',
                  'RatingId', 'ProductReview']


class ShippingAgentsResource(serializers.ModelSerializer):
    class Meta:
        model = ShippingAgents
        fields = ['Id', 'NameA', 'NameL', 'Adress1', 'Adress2',
                  'Phone', 'Email', 'Password', 'PostCode']


class shippingAgentUsersResource(serializers.ModelSerializer):
    class Meta:
        model = ShippingAgentUsers
        fields = ['Id', 'UserId', 'ShippingAgentId']


class shippingDetailsResource(serializers.ModelSerializer):
    class Meta:
        model = ShippingDetails
        fields = ['Id', 'ShippingAgentId', 'OrderId', 'DeliveryNotes']


class specificationValueCountsResource(serializers.ModelSerializer):
    class Meta:
        model = SpecificationValueCounts
        fields = ['SpecificationValue', 'SpecificationCount']


class specificationsResource(serializers.ModelSerializer):
    class Meta:
        model = Specifications
        fields = ['Id', 'NameA', 'NameL', 'ShowInFilter']


class storeShippingAgentsResource(serializers.ModelSerializer):
    class Meta:
        model = StoreShippingAgents
        fields = ['Id', 'StoreId', 'ShippingAgentId']


class storesResource(serializers.ModelSerializer):
    VendorName = serializers.SerializerMethodField('vendorName')
    ShippingAgentName = serializers.SerializerMethodField('shippingAgentName')

    def vendorName(self, request):
        return vendorName()

    def shippingAgentName(self, request):
        return shippingAgentName()

    class Meta:
        model = Stores
        fields = ['Id', 'VendorId', 'VendorName', 'NameA', 'NameL', 'email', 'Address',
                  'CountryId', 'City', 'MapLocation', 'ShippingAgentName', 'ShippingAgentId']


class transactionTypesResource(serializers.ModelSerializer):
    class Meta:
        model = TransactionTypes
        fields = ['Id', 'Code', 'NameA', 'NameL']


class usersResource(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['Id', 'NameA', 'NameL', 'Email', 'Password', 'City']


class vendorPriceListsResource(serializers.ModelSerializer):
    class Meta:
        model = VendorPriceLists
        fields = ['Id', 'VendorId', 'ProductId', 'CountryId', 'Price']


class vendorsResource(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = ['Id', 'NameA', 'NameL', 'Adress1', 'Adress2',
                  'Phone', 'Email', 'Password', 'PostCode']


class getHomeProductsResource(serializers.ModelSerializer):
    class Meta:
        model = GetHomeProducts
        fields = ['Id', 'StoreId', 'ProductId', 'QuantityBalance', 'ProductName',
                  'StoreName', 'ImageUrl', 'ImageUrl6', 'ImageUrl7', 'Description', 'Price',
                  'Currency', 'CategoryId', 'PageNumber', 'FiveStarsCount', 'FourStarsCount',
                  'ThreeStarsCount', 'TwoStarsCount', 'OneStarsCount', 'MaxTotalRating', 'finalProductRating', 'OutOfFivestring']
