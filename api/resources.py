from PyCommerce.models import brands, cartTransactions, cartTransactionMasters, categories, countries, getHomeProducts, inventoryBalances, inventoryDetails, orderMasters, orderStatus, orders, productSpecifications, productStoreRatings, products, shippingAgents, shippingAgentUsers, shippingDetails, specificationValueCounts, specifications, storeShippingAgents, stores, transactionTypes, users, vendorPriceLists, vendors
from rest_framework import serializers


class brandsResource(serializers.ModelSerializer):
    class Meta:
        model = brands
        fields = ['id', 'NameA', 'NameL']


class cartTransactionsResource(serializers.ModelSerializer):
    class Meta:
        model = cartTransactions
        fields = ['id', 'ProductId', 'MasterId',
                  'StoreId', 'Quantity', 'IsOrdered']


class cartTransactionMastersResource(serializers.ModelSerializer):
    class Meta:
        model = cartTransactionMasters
        fields = ['id', 'DateCreated']


class categoriesResource(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = ['id', 'NameA', 'NameL',
                  'Level', 'ImageUrl', 'MainCategoryId']


class countriesResource(serializers.ModelSerializer):
    class Meta:
        model = countries
        fields = ['id', 'NameA', 'NameL', 'Symbol']


class inventoryBalancesResource(serializers.ModelSerializer):
    class Meta:
        model = inventoryBalances
        fields = ['id', 'StoreId', 'ProductId', 'QuantityBalance']


class inventoryDetailsResource(serializers.ModelSerializer):
    StoreName = serializers.SerializerMethodField('storeName')
    ProductName = serializers.SerializerMethodField('productName')
    Quantitys = serializers.SerializerMethodField('quantity')

    def storeName(self, obj):
        return obj.StoreId.NameL

    def productName(self, obj):
        return obj.ProductId.NameL

    def quantity(self, obj):
        print(obj.Quantity)
        return 1

    class Meta:
        model = inventoryDetails
        fields = ['id', 'StoreName', 'ProductName', 'Quantitys']


class orderMastersResource(serializers.ModelSerializer):
    class Meta:
        model = orderMasters
        fields = ['id', 'cartId', 'UserId', 'DateCreated',
                  'ShippingAdress', 'OrderStatusId']


class orderStatusResource(serializers.ModelSerializer):
    class Meta:
        model = orderStatus
        fields = ['id', 'Code', 'StatusNameA', 'StatusNameL']


class ordersResource(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = ['ProductId', 'StoreId', 'cartId', 'MasterId', 'UserId', 'Quantity',
                  'ShippingAgentId', 'UnitPrice', 'TotalPrice', 'isDelivered', 'MapLocation',
                  'DeliveredByUserId', 'Latitude', 'Longitude']


class productsResource(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ['id', 'NameA', 'NameL', 'ImageUrl', 'ImageUrl6',
                  'ImageUrl7', 'CategoryId', 'BrandId', 'Description']


class productSpecificationsResource(serializers.ModelSerializer):
    class Meta:
        model = productSpecifications
        fields = ['id', 'CategoryId', 'ProductId', 'SpecificationId',
                  'SpecificationName', 'SpecificationValue', 'ShowInFilter']


class productStoreRatingsResource(serializers.ModelSerializer):
    class Meta:
        model = productStoreRatings
        fields = ['id', 'ProductId', 'StoreId', 'UserId',
                  'RatingId', 'ProductReview']


class shippingAgentsResource(serializers.ModelSerializer):
    class Meta:
        model = shippingAgents
        fields = ['id', 'NameA', 'NameL', 'Adress1', 'Adress2',
                  'Phone', 'Email', 'Password', 'PostCode']


class shippingAgentUsersResource(serializers.ModelSerializer):
    UserName = serializers.SerializerMethodField('userName')
    ShippingAgentName = serializers.SerializerMethodField('shippingAgentName')

    def userName(self, obj):
        return obj.UserId.NameL

    def shippingAgentName(self, obj):
        return obj.ShippingAgentId.NameL

    class Meta:
        model = shippingAgentUsers
        fields = ['id', 'UserName', 'ShippingAgentName']


class shippingDetailsResource(serializers.ModelSerializer):
    class Meta:
        model = shippingDetails
        fields = ['id', 'ShippingAgentId', 'OrderId', 'DeliveryNotes']


class specificationValueCountsResource(serializers.ModelSerializer):
    class Meta:
        model = specificationValueCounts
        fields = ['SpecificationValue', 'SpecificationCount']


class specificationsResource(serializers.ModelSerializer):
    class Meta:
        model = specifications
        fields = ['id', 'NameA', 'NameL', 'ShowInFilter']


class storeShippingAgentsResource(serializers.ModelSerializer):
    class Meta:
        model = storeShippingAgents
        fields = ['id', 'StoreId', 'ShippingAgentId']


class storesResource(serializers.ModelSerializer):
    ShippingAgentName = serializers.SerializerMethodField('shippingAgentName')
    VendorName = serializers.SerializerMethodField('vendorName')
    CountryName = serializers.SerializerMethodField('countryName')

    def shippingAgentName(self, obj):
        return obj.ShippingAgentId.NameL

    def vendorName(self, obj):
        return obj.VendorId.NameL

    def countryName(self, obj):
        return obj.CountryId.NameL

    class Meta:
        model = stores
        fields = ['id', 'NameA', 'NameL', 'Email', 'Address', 'VendorId',
                  'CountryId', 'City', 'ShippingAgentName', 'VendorName', 'CountryName']


class transactionTypesResource(serializers.ModelSerializer):
    class Meta:
        model = transactionTypes
        fields = ['id', 'Code', 'NameA', 'NameL']


class usersResource(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['id', 'NameA', 'NameL', 'Email', 'Password', 'City']


class vendorPriceListsResource(serializers.ModelSerializer):
    VendorName = serializers.SerializerMethodField('vendorName')
    ProductName = serializers.SerializerMethodField('productName')
    CountryName = serializers.SerializerMethodField('countryName')

    def vendorName(self, obj):
        return obj.VendorId.NameL

    def productName(self, obj):
        return obj.ProductId.NameL

    def countryName(self, obj):
        return obj.CountryId.NameL

    class Meta:
        model = vendorPriceLists
        fields = ['id', 'VendorName', 'ProductName', 'CountryName', 'Price']


class vendorsResource(serializers.ModelSerializer):
    class Meta:
        model = vendors
        fields = ['id', 'NameA', 'NameL', 'Adress1', 'Adress2',
                  'Phone', 'Email', 'Password', 'PostCode']


class getHomeProductsResource(serializers.ModelSerializer):
    class Meta:
        model = getHomeProducts
        fields = ['id', 'StoreId', 'ProductId', 'QuantityBalance', 'ProductName',
                  'StoreName', 'ImageUrl', 'ImageUrl6', 'ImageUrl7', 'Description', 'Price',
                  'Currency', 'CategoryId', 'PageNumber', 'FiveStarsCount', 'FourStarsCount',
                  'ThreeStarsCount', 'TwoStarsCount', 'OneStarsCount', 'MaxTotalRating', 'finalProductRating', 'OutOfFivestring']
