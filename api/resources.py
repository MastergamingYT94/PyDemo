from PyDemo.settings import SITE_URL
from PyCommerce.models import brands, cartTransactions, cartTransactionMasters, categories, countries, getHomeProducts, inventoryBalances, inventoryDetails, orderMasters, orderStatus, orders, productSpecifications, productStoreRatings, products, shippingAgents, shippingAgentUsers, shippingDetails, specificationValueCount, specifications, starPercent, storeShippingAgents, stores, transactionTypes, users, vendorPriceLists, vendors
from rest_framework import serializers
from django.db.models import Sum


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


class cartItemsResource(serializers.ModelSerializer):
    NameA = serializers.SerializerMethodField('product_nameA')
    NameL = serializers.SerializerMethodField('product_nameL')
    Description = serializers.SerializerMethodField('product_desc')
    Currency = serializers.SerializerMethodField('product_currency')
    Image = serializers.SerializerMethodField('product_img')
    Image2 = serializers.SerializerMethodField('product_img2')
    Image3 = serializers.SerializerMethodField('product_img3')
    Image4 = serializers.SerializerMethodField('product_img4')
    Price = serializers.SerializerMethodField('product_price')
    productReview = serializers.SerializerMethodField('product_review')
    StoreName = serializers.SerializerMethodField('store_name')

    def product_nameA(self, obj):
        return obj.ProductId.NameA

    def product_nameL(self, obj):
        return obj.ProductId.NameL

    def product_desc(self, obj):
        return obj.ProductId.Description

    def product_currency(self, obj):
        store = [store.CountryId.id for store in stores.objects.filter(
            id=obj.StoreId.id)]
        Country = countries.objects.filter(
            id__in=store).values_list('Symbol', flat=True)
        for country in Country:
            return country

    def product_img(self, obj):
        Image = None
        product = [item.Image for item in products.objects.filter(
            id=obj.ProductId.id)]
        for item in product:
            if item:
                Image = SITE_URL + item.url
        return Image

    def product_img2(self, obj):
        Image = None
        product = [item.Image2 for item in products.objects.filter(
            id=obj.ProductId.id)]
        for item in product:
            if item:
                Image = SITE_URL + item.url
        return Image

    def product_img3(self, obj):
        Image = None
        product = [item.Image3 for item in products.objects.filter(
            id=obj.ProductId.id)]
        for item in product:
            if item:
                Image = SITE_URL + item.url
        return Image

    def product_img4(self, obj):
        Image = None
        product = [item.Image4 for item in products.objects.filter(
            id=obj.ProductId.id)]
        for item in product:
            if item:
                Image = SITE_URL + item.url
        return Image

    def product_price(self, obj):
        store = stores.objects.filter(id=obj.StoreId.id)
        product = [product.id for product in products.objects.filter(
            id=obj.ProductId.id)]
        country = [store.CountryId for store in store]
        vendor = [store.VendorId for store in store]
        Price = vendorPriceLists.objects.filter(
            CountryId__in=country, ProductId__in=product, VendorId__in=vendor).values_list('Price', flat=True)
        for price in Price:
            return price

    def product_review(self, obj):
        return ""

    def store_name(self, obj):
        return obj.StoreId.NameL

    class Meta:
        model = inventoryBalances
        fields = ['id', 'ProductId', 'StoreId', 'NameA', 'NameL',
                  'Description', 'Currency', 'Image', 'Image2', 'Image3', 'Image4', 'Price', 'productReview', 'StoreName']


class cartResource(serializers.ModelSerializer):
    ProductName = serializers.SerializerMethodField('product_name')
    Image = serializers.SerializerMethodField('product_img')
    Description = serializers.SerializerMethodField('product_desc')
    StoreName = serializers.SerializerMethodField('store_name')
    Longitude = serializers.SerializerMethodField('store_lon')
    Latitude = serializers.SerializerMethodField('store_lat')
    TotalPrice = serializers.SerializerMethodField('total_price')
    TotalPricePerItem = serializers.SerializerMethodField('price')
    Currency = serializers.SerializerMethodField('currency')
    InventoryBalanceId = serializers.SerializerMethodField('inv_balance')
    ShippingAgentId = serializers.SerializerMethodField('agent_id')

    def product_name(self, obj):
        return obj.ProductId.NameL

    def product_img(self, obj):
        Image = None
        if obj.ProductId.Image:
            Image = SITE_URL + obj.ProductId.Image.url
        return Image

    def product_desc(self, obj):
        return obj.ProductId.Description

    def store_name(self, obj):
        return obj.StoreId.NameL

    def store_lon(self, obj):
        return obj.StoreId.Longitude

    def store_lat(self, obj):
        return obj.StoreId.Latitude

    def total_price(self, obj):
        store = stores.objects.filter(id=obj.StoreId.id)
        product = [product.id for product in products.objects.filter(
            id=obj.ProductId.id)]
        country = [store.CountryId for store in store]
        vendor = [store.VendorId for store in store]
        Price = vendorPriceLists.objects.filter(
            CountryId__in=country, ProductId__in=product, VendorId__in=vendor).values_list('Price', flat=True)
        for price in Price:
            return price * obj.Quantity

    def price(self, obj):
        store = stores.objects.filter(id=obj.StoreId.id)
        product = [product.id for product in products.objects.filter(
            id=obj.ProductId.id)]
        country = [store.CountryId for store in store]
        vendor = [store.VendorId for store in store]
        Price = vendorPriceLists.objects.filter(
            CountryId__in=country, ProductId__in=product, VendorId__in=vendor).values_list('Price', flat=True)
        for price in Price:
            return price

    def currency(self, obj):
        store = [store.CountryId.id for store in stores.objects.filter(
            id=obj.StoreId.id)]
        Country = countries.objects.filter(
            id__in=store).values_list('Symbol', flat=True)
        for country in Country:
            return country

    def inv_balance(self, obj):
        store = [store.id for store in stores.objects.filter(
            id=obj.StoreId.id)]
        product = [product.id for product in products.objects.filter(
            id=obj.ProductId.id)]
        items = inventoryBalances.objects.filter(
            ProductId__in=product, StoreId__in=store).values_list('id', flat=True)
        for item in items:
            return item

    def agent_id(self, obj):
        agents = [item.ShippingAgentId.id for item in storeShippingAgents.objects.filter(
            StoreId=obj.StoreId.id)]
        for agent in agents:
            return agent

    class Meta:
        model = cartTransactions
        fields = ['id', 'ProductId', 'StoreId', 'MasterId', 'Quantity',
                  'ProductName', 'StoreName', 'Image', 'Description',
                  'TotalPrice', 'TotalPricePerItem', 'Currency', 'InventoryBalanceId',
                  'ShippingAgentId', 'Longitude', 'Latitude']


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

    def storeName(self, obj):
        return obj.StoreId.NameL

    def productName(self, obj):
        return obj.ProductId.NameL

    class Meta:
        model = inventoryDetails
        fields = ['id', 'StoreId', 'ProductId',
                  'StoreName', 'ProductName', 'Quantity']


class orderMastersResource(serializers.ModelSerializer):
    Username = serializers.SerializerMethodField('user_name')
    OrderTotal = serializers.SerializerMethodField('order_total')

    def user_name(self, obj):
        return obj.UserId.NameL

    def order_total(self, obj):
        total = orders.objects.filter(
            MasterId=obj.id).aggregate(Sum('TotalPrice'))
        return total['TotalPrice__sum']

    class Meta:
        model = orderMasters
        fields = ['id', 'cartId', 'UserId', 'DateCreated',
                  'ShippingAddress', 'OrderStatusId', 'Username', 'OrderTotal']


class orderStatusResource(serializers.ModelSerializer):
    class Meta:
        model = orderStatus
        fields = ['id', 'Code', 'StatusNameA', 'StatusNameL']


class ordersResource(serializers.ModelSerializer):
    VendorName = serializers.SerializerMethodField('vendor_name')
    ProductName = serializers.SerializerMethodField('product_name')
    Image = serializers.SerializerMethodField('product_img')
    StoreName = serializers.SerializerMethodField('store_name')
    Longitude = serializers.SerializerMethodField('store_lon')
    Latitude = serializers.SerializerMethodField('store_lat')
    Currency = serializers.SerializerMethodField('currency')
    UnitPrice = serializers.SerializerMethodField('price')
    TotalPrice = serializers.SerializerMethodField('total_price')
    DeliveryNote = serializers.SerializerMethodField('note')
    Status = serializers.SerializerMethodField('status')
    InventoryBalanceId = serializers.SerializerMethodField('inv_id')
    DeliveredByUserId = serializers.SerializerMethodField('note_id')

    def vendor_name(self, obj):
        vendors = [item.VendorId.NameL for item in stores.objects.filter(
            id=obj.StoreId.id)]
        for vendor in vendors:
            return vendor

    def product_name(self, obj):
        return obj.ProductId.NameL

    def product_img(self, obj):
        Image = None
        if obj.ProductId.Image:
            Image = SITE_URL + obj.ProductId.Image.url
        return Image

    def store_name(self, obj):
        return obj.StoreId.NameL

    def store_lon(self, obj):
        return obj.StoreId.Longitude

    def store_lat(self, obj):
        return obj.StoreId.Latitude

    def total_price(self, obj):
        store = stores.objects.filter(id=obj.StoreId.id)
        product = [product.id for product in products.objects.filter(
            id=obj.ProductId.id)]
        country = [store.CountryId for store in store]
        vendor = [store.VendorId for store in store]
        Price = vendorPriceLists.objects.filter(
            CountryId__in=country, ProductId__in=product, VendorId__in=vendor).values_list('Price', flat=True)
        for price in Price:
            return price * obj.Quantity

    def price(self, obj):
        store = stores.objects.filter(id=obj.StoreId.id)
        product = [product.id for product in products.objects.filter(
            id=obj.ProductId.id)]
        country = [store.CountryId for store in store]
        vendor = [store.VendorId for store in store]
        Price = vendorPriceLists.objects.filter(
            CountryId__in=country, ProductId__in=product, VendorId__in=vendor).values_list('Price', flat=True)
        for price in Price:
            return price

    def currency(self, obj):
        store = [store.CountryId.id for store in stores.objects.filter(
            id=obj.StoreId.id)]
        Country = countries.objects.filter(
            id__in=store).values_list('Symbol', flat=True)
        for country in Country:
            return country

    def inv_id(self, obj):
        store = [store.id for store in stores.objects.filter(
            id=obj.StoreId.id)]
        product = [product.id for product in products.objects.filter(
            id=obj.ProductId.id)]
        items = inventoryBalances.objects.filter(
            ProductId__in=product, StoreId__in=store).values_list('id', flat=True)
        for item in items:
            return item

    def agent_id(self, obj):
        agents = [item.ShippingAgentId.id for item in storeShippingAgents.objects.filter(
            StoreId=obj.StoreId.id)]
        for agent in agents:
            return agent

    def note_id(self, obj):
        return obj.UserId.id

    def status(self, obj):
        master = [item.OrderStatusId.id for item in orderMasters.objects.filter(
            id=obj.MasterId.id)]
        code = [item.Code for item in orderStatus.objects.filter(
            Code__in=master)]
        for code in code:
            return code

    def note(self, obj):
        return ""

    class Meta:
        model = orders
        fields = ['id', 'ProductId', 'StoreId', 'cartId', 'MasterId', 'UserId', 'Quantity',
                  'InventoryBalanceId', 'Currency', 'ProductName', 'Image',
                  'DeliveryNote', 'Status', 'DeliveredByUserId', 'Latitude', 'Longitude', 'VendorName',
                  'StoreName', 'ShippingAgentId', 'UnitPrice', 'TotalPrice', 'isDelivered']


class productsResource(serializers.ModelSerializer):
    Image = serializers.SerializerMethodField('img')
    Image2 = serializers.SerializerMethodField('img2')
    Image3 = serializers.SerializerMethodField('img3')
    Image4 = serializers.SerializerMethodField('img4')
    ImageUrl = serializers.SerializerMethodField('img_url')
    ImageUrl2 = serializers.SerializerMethodField('img2_url')
    ImageUrl3 = serializers.SerializerMethodField('img3_url')

    def img(self, obj):
        return obj.Image.name

    def img2(self, obj):
        return obj.Image2.name

    def img3(self, obj):
        return obj.Image3.name

    def img4(self, obj):
        return obj.Image4

    def img_url(self, obj):
        Image = None
        if obj.Image:
            Image = SITE_URL + obj.Image.url
        return Image

    def img2_url(self, obj):
        Image = None
        if obj.Image2:
            Image = SITE_URL + obj.Image2.url
        return Image

    def img3_url(self, obj):
        Image = None
        if obj.Image3:
            Image = SITE_URL + obj.Image3.url
        return Image

    class Meta:
        model = products
        fields = ['id', 'NameA', 'NameL', 'Image', 'Image2', 'Image3',
                  'Image4', 'ImageUrl', 'ImageUrl2', 'ImageUrl3',
                  'CategoryId', 'BrandId', 'Description']


class productSpecificationsResource(serializers.ModelSerializer):
    ProductName = serializers.SerializerMethodField('product_name')

    def product_name(self, obj):
        return obj.ProductId.NameL

    class Meta:
        model = productSpecifications
        fields = ['id', 'CategoryId', 'ProductId', 'ProductName', 'SpecificationId',
                  'SpecificationName', 'SpecificationValue', 'ShowInFilter']


class productSpecificationsInvResource(serializers.ModelSerializer):
    SpecificationName = serializers.SerializerMethodField('specname')
    ProductName = serializers.SerializerMethodField('product')

    def specname(self, obj):
        return obj.SpecificationId.NameL

    def product(self, obj):
        return obj.ProductId.NameL

    class Meta:
        model = productSpecifications
        fields = ['id', 'ProductId', 'ProductName',
                  'SpecificationName', 'SpecificationValue']


class productStoreRatingsResource(serializers.ModelSerializer):
    UserName = serializers.SerializerMethodField('user')
    ProductRate = serializers.SerializerMethodField('rating')

    def user(self, obj):
        return obj.UserId.NameL

    def rating(self, obj):
        rating = (obj.RatingId / 5) * 100
        return rating

    class Meta:
        model = productStoreRatings
        fields = ['id', 'ProductRate', 'UserName', 'ProductReview']


class shippingAgentsResource(serializers.ModelSerializer):
    class Meta:
        model = shippingAgents
        fields = ['id', 'NameA', 'NameL', 'Address1', 'Address2',
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
        fields = ['id', 'ShippingAgentId', 'UserName', 'ShippingAgentName']


class shippingDetailsResource(serializers.ModelSerializer):
    class Meta:
        model = shippingDetails
        fields = ['id', 'ShippingAgentId', 'OrderId', 'DeliveryNotes']


class specificationsResource(serializers.ModelSerializer):
    class Meta:
        model = specifications
        fields = ['id', 'NameA', 'NameL', 'ShowInFilter']


class SpecificationsResource(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    NameA = serializers.SerializerMethodField('get_nameA')
    NameL = serializers.SerializerMethodField('get_nameL')
    ShowInFilter = serializers.SerializerMethodField('get_filter')
    IsSelected = serializers.SerializerMethodField('is_selected')

    def get_id(self, obj):
        return obj.SpecificationId.id

    def get_nameA(self, obj):
        return obj.SpecificationId.NameA

    def get_nameL(self, obj):
        return obj.SpecificationId.NameL

    def get_filter(self, obj):
        return obj.SpecificationId.ShowInFilter

    def is_selected(self, obj):
        return True

    class Meta:
        model = productSpecifications
        fields = ['id', 'CategoryId', 'NameA',
                  'NameL', 'ShowInFilter', 'IsSelected']


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
                  'CountryId', 'City', 'ShippingAgentName', 'ShippingAgentId', 'VendorName', 'CountryName']


class transactionTypesResource(serializers.ModelSerializer):
    class Meta:
        model = transactionTypes
        fields = ['id', 'Code', 'NameA', 'NameL']


class usersResource(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['id', 'NameA', 'NameL', 'Email', 'Password',
                  'Address1', 'Address2', 'Phone', 'City']


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
        fields = ['id', 'VendorId', 'ProductId', 'CountryId',
                  'VendorName', 'ProductName', 'CountryName', 'Price']


class vendorsResource(serializers.ModelSerializer):
    class Meta:
        model = vendors
        fields = ['id', 'NameA', 'NameL', 'Address1', 'Address2',
                  'Phone', 'Email', 'Password', 'PostCode']


class getHomeProductsResource(serializers.ModelSerializer):
    Image = serializers.SerializerMethodField('image')

    def image(self, obj):
        Image = None
        if obj.ProductId.Image:
            if obj.ProductId.Image.url:
                Image = SITE_URL + obj.ProductId.Image.url
        return Image

    class Meta:
        model = getHomeProducts
        fields = ['id', 'StoreId', 'ProductId', 'QuantityBalance', 'ProductName',
                  'StoreName', 'Image', 'Description', 'Price',
                  'Currency', 'CategoryId', 'PageNumber', 'FiveStarsCount', 'FourStarsCount',
                  'ThreeStarsCount', 'TwoStarsCount', 'OneStarsCount', 'MaxTotalRating', 'finalProductRating', 'OutOfFivestring']


class specificationValueCountResource(serializers.ModelSerializer):
    isSelected = serializers.SerializerMethodField('is_selected')

    def is_selected(self, obj):
        return False

    class Meta:
        model = specificationValueCount
        fields = ['id', 'SpecificationId', 'SpecificationValue',
                  'SpecificationCount', 'CategoryId', 'isSelected']


class starPercentResource(serializers.ModelSerializer):
    class Meta:
        model = starPercent
        fields = ['id', 'ProductId', 'StoreId', 'FiveStarsCount', 'FourStarsCount', 'ThreeStarsCount',
                  'TwoStarsCount', 'OneStarCount', 'FiveStarsPercent', 'FourStarsPercent', 'ThreeStarsPercent',
                  'TwoStarsPercent', 'OneStarPercent', 'averageRating', 'OutOfFive', 'allReviewsCount']
