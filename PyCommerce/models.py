from django.db import models
# Create your models here.


class brands(models.Model):
    NameA = models.CharField(max_length=2550, blank=True)
    NameL = models.CharField(max_length=2550)


class cartTransactionMasters(models.Model):
    DateCreated = models.DateTimeField()


class categories(models.Model):
    MainCategoryId = models.ForeignKey(
        'self', on_delete=models.DO_NOTHING, db_column='MainCategoryId', blank=True, db_constraint=False)
    NameA = models.CharField(max_length=2550, blank=True)
    NameL = models.CharField(max_length=2550)
    Level = models.IntegerField()
    ImageUrl = models.CharField(max_length=2550, blank=True)


class countries(models.Model):
    NameA = models.CharField(max_length=2550, blank=True)
    NameL = models.CharField(max_length=2550)
    Symbol = models.CharField(max_length=2550)


class orderStatus(models.Model):
    Code = models.IntegerField()
    StatusNameA = models.CharField(max_length=2550, blank=True)
    StatusNameL = models.CharField(max_length=2550)


class shippingAgents(models.Model):
    NameA = models.CharField(max_length=2550, blank=True)
    NameL = models.CharField(max_length=2550)
    Adress1 = models.CharField(max_length=2550)
    Adress2 = models.CharField(max_length=2550, blank=True)
    Phone = models.CharField(max_length=2550, blank=True)
    Email = models.CharField(max_length=2550)
    Password = models.CharField(max_length=2550)
    PostCode = models.CharField(max_length=2550, blank=True)

    def __str__(self):
        return self.NameL


class specificationValueCounts(models.Model):
    SpecificationValue = models.CharField(max_length=2550, primary_key=True)
    SpecificationCount = models.IntegerField()


class specifications(models.Model):
    NameA = models.CharField(max_length=2550, blank=True)
    NameL = models.CharField(max_length=2550)
    ShowInFilter = models.IntegerField()


class transactionTypes(models.Model):
    Code = models.IntegerField()
    NameA = models.CharField(max_length=2550, blank=True)
    NameL = models.CharField(max_length=2550)


class users(models.Model):
    NameA = models.CharField(max_length=2550, blank=True)
    NameL = models.CharField(max_length=2550)
    Email = models.CharField(max_length=2550)
    Password = models.CharField(max_length=2550)
    City = models.CharField(max_length=2550)


class vendors(models.Model):
    NameA = models.CharField(max_length=2550, blank=True)
    NameL = models.CharField(max_length=2550)
    Adress1 = models.CharField(max_length=2550)
    Adress2 = models.CharField(max_length=2550, blank=True)
    Phone = models.CharField(max_length=2550, blank=True)
    Email = models.CharField(max_length=2550)
    Password = models.CharField(max_length=2550)
    PostCode = models.CharField(max_length=2550, blank=True)


class products(models.Model):
    NameA = models.CharField(max_length=2550, blank=True)
    NameL = models.CharField(max_length=2550)
    ImageUrl = models.CharField(max_length=12550, blank=True)
    ImageUrl6 = models.CharField(max_length=12550, blank=True)
    ImageUrl7 = models.CharField(max_length=12550, blank=True)
    Description = models.CharField(max_length=2550, blank=True)
    BrandId = models.ForeignKey(
        brands, on_delete=models.DO_NOTHING,  db_column='BrandId')
    CategoryId = models.ForeignKey(
        categories, on_delete=models.DO_NOTHING,  db_column='CategoryId')


class vendorPriceLists(models.Model):
    VendorId = models.ForeignKey(
        vendors, on_delete=models.DO_NOTHING,  db_column='VendorId')
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING,  db_column='ProductId')
    CountryId = models.ForeignKey(
        countries, on_delete=models.DO_NOTHING,  db_column='CountryId')
    Price = models.FloatField()


class productSpecifications(models.Model):
    SpecificationName = models.CharField(max_length=2550)
    SpecificationValue = models.CharField(max_length=2550)
    ShowInFilter = models.IntegerField()
    CategoryId = models.ForeignKey(
        categories, on_delete=models.DO_NOTHING,  db_column='CategoryId')
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING,  db_column='ProductId')
    SpecificationId = models.ForeignKey(
        specifications, on_delete=models.DO_NOTHING,  db_column='SpecificationId')


class stores(models.Model):
    NameA = models.CharField(max_length=2550, blank=True)
    NameL = models.CharField(max_length=2550)
    Email = models.CharField(max_length=2550)
    Address = models.CharField(max_length=2550, blank=True)
    City = models.CharField(max_length=2550)
    Latitude = models.CharField(max_length=2550, blank=True)
    Longitude = models.CharField(max_length=2550, blank=True)
    CountryId = models.ForeignKey(
        countries, on_delete=models.DO_NOTHING,  db_column='CountryId')
    VendorId = models.ForeignKey(
        vendors, on_delete=models.DO_NOTHING,  db_column='VendorId')
    ShippingAgentId = models.ForeignKey(
        shippingAgents, on_delete=models.DO_NOTHING,  db_column='ShippingAgentId')


class storeShippingAgents(models.Model):
    StoreId = models.ForeignKey(
        stores, on_delete=models.DO_NOTHING, db_column='StoreId')
    ShippingAgentId = models.ForeignKey(
        shippingAgents, on_delete=models.DO_NOTHING,  db_column='ShippingAgentId')


class shippingAgentUsers(models.Model):
    UserId = models.ForeignKey(
        users, on_delete=models.DO_NOTHING,  db_column='UserId')
    ShippingAgentId = models.ForeignKey(
        shippingAgents, on_delete=models.DO_NOTHING,  db_column='ShippingAgentId')


class inventoryBalances(models.Model):
    StoreId = models.ForeignKey(
        stores, on_delete=models.DO_NOTHING, db_column='StoreId')
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING,  db_column='ProductId')
    QuantityBalance = models.FloatField()


class inventoryDetails(models.Model):
    StoreId = models.ForeignKey(
        stores, on_delete=models.DO_NOTHING, db_column='StoreId')
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING,  db_column='ProductId')
    Quantity = models.FloatField(blank=False)


class orderMasters(models.Model):
    cartId = models.IntegerField()
    DateCreated = models.DateTimeField()
    ShippingAdress = models.CharField(max_length=2550, blank=True)
    UserId = models.IntegerField()
    OrderStatusId = models.IntegerField()


class cartTransactions(models.Model):
    Quantity = models.FloatField()
    IsOrdered = models.IntegerField()
    ProductId = models.IntegerField()
    MasterId = models.IntegerField()
    StoreId = models.IntegerField()


class orders(models.Model):
    UnitPrice = models.FloatField()
    TotalPrice = models.FloatField()
    isDelivered = models.IntegerField(blank=True)
    Latitude = models.CharField(max_length=2550, blank=True)
    Longitude = models.CharField(max_length=2550, blank=True)
    cartId = models.IntegerField()
    Quantity = models.FloatField()
    DeliveredByUserId = models.IntegerField()
    ProductId = models.IntegerField()
    StoreId = models.IntegerField()
    MasterId = models.IntegerField()
    UserId = models.IntegerField()
    ShippingAgentId = models.IntegerField()


class shippingDetails(models.Model):
    DeliveryNotes = models.CharField(max_length=2550, blank=True)
    OrderId = models.ForeignKey(
        orders, on_delete=models.DO_NOTHING, db_column='OrderId')
    ShippingAgentId = models.ForeignKey(
        shippingAgents, on_delete=models.DO_NOTHING,  db_column='ShippingAgentId')


class productStoreRatings(models.Model):
    RatingId = models.IntegerField()
    ProductReview = models.CharField(max_length=2550, blank=True)
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING,  db_column='ProductId')
    StoreId = models.ForeignKey(
        stores, on_delete=models.DO_NOTHING, db_column='StoreId')
    UserId = models.ForeignKey(
        users, on_delete=models.DO_NOTHING,  db_column='UserId')


class getHomeProducts(models.Model):
    StoreId = models.IntegerField()
    ProductId = models.IntegerField()
    QuantityBalance = models.FloatField()
    ProductName = models.CharField(max_length=2550)
    StoreName = models.CharField(max_length=2550)
    ImageUrl = models.CharField(max_length=2550)
    ImageUrl6 = models.CharField(max_length=2550)
    ImageUrl7 = models.CharField(max_length=2550)
    Description = models.CharField(max_length=2550)
    Price = models.FloatField()
    Currency = models.CharField(max_length=2550)
    CategoryId = models.IntegerField()
    PageNumber = models.IntegerField()
    FiveStarsCount = models.FloatField()
    FourStarsCount = models.FloatField()
    ThreeStarsCount = models.FloatField()
    TwoStarsCount = models.FloatField()
    OneStarsCount = models.FloatField()
    MaxTotalRating = models.FloatField()
    finalProductRating = models.FloatField()
    OutOfFivestring = models.FloatField()

    class Meta:
        managed = False
        db_table = "GetHomeProducts"
