from django.db import models
# Create your models here.


class brands(models.Model):

    Id = models.AutoField(primary_key=True)
    NameA = models.CharField(max_length=2550)
    NameL = models.CharField(max_length=2550)


class cartTransaction(models.Model):

    Id = models.AutoField(primary_key=True)
    ProductId = models.IntegerField()
    MasterId = models.IntegerField()
    StoreId = models.IntegerField()
    Quantity = models.FloatField()
    IsOrdered = models.IntegerField()


class cartTransactionMaster(models.Model):

    Id = models.AutoField(primary_key=True)
    DateCreated = models.DateTimeField()


class category(models.Model):

    Id = models.AutoField(primary_key=True)
    MainCategoryId = models.IntegerField()
    NameA = models.CharField(max_length=2550)
    NameL = models.CharField(max_length=2550)
    Level = models.IntegerField()
    ImageUrl = models.CharField(max_length=2550)


class countries(models.Model):

    Id = models.AutoField(primary_key=True)
    NameA = models.CharField(max_length=2550)
    NameL = models.CharField(max_length=2550)
    Symbol = models.CharField(max_length=2550)


class inventoryBalance(models.Model):

    Id = models.AutoField(primary_key=True)
    StoreId = models.IntegerField()
    ProductId = models.IntegerField()
    QuantityBalance = models.FloatField()


class inventoryDetail(models.Model):

    Id = models.AutoField(primary_key=True)
    TransType = models.IntegerField()
    TransDate = models.DateField()
    StoreId = models.IntegerField()
    ProductId = models.IntegerField()
    Quantity = models.FloatField()


class orderMaster(models.Model):

    Id = models.AutoField(primary_key=True)
    cartId = models.IntegerField()
    UserId = models.IntegerField()
    DateCreated = models.DateTimeField()
    ShippingAdress = models.CharField(max_length=2550)
    OrderStatusId = models.IntegerField()


class orderStatus(models.Model):

    Id = models.AutoField(primary_key=True)
    Code = models.IntegerField()
    StatusNameA = models.CharField(max_length=2550)
    StatusNameL = models.CharField(max_length=2550)


class orders(models.Model):

    Id = models.AutoField(primary_key=True)
    ProductId = models.IntegerField()
    StoreId = models.IntegerField()
    cartId = models.IntegerField()
    MasterId = models.IntegerField()
    UserId = models.IntegerField()
    Quantity = models.FloatField()
    ShippingAgentId = models.IntegerField()
    UnitPrice = models.FloatField()
    TotalPrice = models.FloatField()
    isDelivered = models.IntegerField()
    MapLocation = models.CharField(max_length=2550)
    DeliveredByUserId = models.IntegerField()
    Latitude = models.CharField(max_length=2550)
    Longitude = models.CharField(max_length=2550)


class products(models.Model):

    Id = models.AutoField(primary_key=True)
    NameA = models.CharField(max_length=2550)
    NameL = models.CharField(max_length=2550)
    ImageUrl = models.CharField(max_length=2550)
    ImageUrl6 = models.CharField(max_length=2550)
    ImageUrl7 = models.CharField(max_length=2550)
    CategoryId = models.IntegerField()
    BrandId = models.IntegerField()
    Description = models.CharField(max_length=2550)


class productSpecifications(models.Model):

    Id = models.AutoField(primary_key=True)
    CategoryId = models.IntegerField()
    ProductId = models.IntegerField()
    SpecificationId = models.IntegerField()
    SpecificationName = models.CharField(max_length=2550)
    SpecificationValue = models.CharField(max_length=2550)
    ShowInFilter = models.IntegerField()


class productStoreRating(models.Model):

    Id = models.AutoField(primary_key=True)
    ProductId = models.IntegerField()
    StoreId = models.IntegerField()
    UserId = models.IntegerField()
    RatingId = models.IntegerField()
    ProductReview = models.CharField(max_length=2550)


class shippingAgent(models.Model):

    Id = models.AutoField(primary_key=True)
    NameA = models.CharField(max_length=2550)
    NameL = models.CharField(max_length=2550)
    Adress1 = models.CharField(max_length=2550)
    Adress2 = models.CharField(max_length=2550)
    Phone = models.CharField(max_length=2550)
    Email = models.CharField(max_length=2550)
    Password = models.CharField(max_length=2550)
    PostCode = models.CharField(max_length=2550)


class shippingAgentUser(models.Model):

    Id = models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    ShippingAgentId = models.IntegerField()


class shippingDetails(models.Model):

    Id = models.AutoField(primary_key=True)
    ShippingAgentId = models.IntegerField()
    OrderId = models.IntegerField()
    DeliveryNotes = models.CharField(max_length=2550)


class specificationValueCounts(models.Model):

    SpecificationValue = models.CharField(max_length=2550, primary_key=True)
    SpecificationCount = models.IntegerField()


class specifications(models.Model):

    Id = models.AutoField(primary_key=True)
    NameA = models.CharField(max_length=2550)
    NameL = models.CharField(max_length=2550)
    ShowInFilter = models.IntegerField()


class storeShippingAgent(models.Model):

    Id = models.IntegerField(primary_key=True)
    StoreId = models.IntegerField()
    ShippingAgentId = models.IntegerField()


class stores(models.Model):

    Id = models.AutoField(primary_key=True)
    VendorId = models.IntegerField()
    NameA = models.CharField(max_length=2550)
    NameL = models.CharField(max_length=2550)
    email = models.CharField(max_length=2550)
    Address = models.CharField(max_length=2550)
    CountryId = models.IntegerField()
    City = models.CharField(max_length=2550)
    MapLocation = models.CharField(max_length=2550)
    ShippingAgentId = models.IntegerField()


class transactionType(models.Model):

    Id = models.AutoField(primary_key=True)
    Code = models.IntegerField()
    NameA = models.CharField(max_length=2550)
    NameL = models.CharField(max_length=2550)


class users(models.Model):

    Id = models.AutoField(primary_key=True)
    NameA = models.CharField(max_length=2550)
    NameL = models.CharField(max_length=2550)
    Email = models.CharField(max_length=2550)
    Password = models.CharField(max_length=2550)
    City = models.CharField(max_length=2550)


class vendorPriceList(models.Model):

    Id = models.AutoField(primary_key=True)
    VendorId = models.IntegerField()
    ProductId = models.IntegerField()
    CountryId = models.IntegerField()
    Price = models.FloatField()


class vendors(models.Model):

    Id = models.AutoField(primary_key=True)
    NameA = models.CharField(max_length=2550)
    NameL = models.CharField(max_length=2550)
    Adress1 = models.CharField(max_length=2550)
    Adress2 = models.CharField(max_length=2550)
    Phone = models.CharField(max_length=2550)
    Email = models.CharField(max_length=2550)
    Password = models.CharField(max_length=2550)
    PostCode = models.CharField(max_length=2550)


class getHomeProducts(models.Model):

    Id = models.AutoField(primary_key=True)
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
