from django.db import models
from cloudinary.models import CloudinaryField


class brands(models.Model):
    NameA = models.TextField(max_length=2550, null=True)
    NameL = models.TextField(max_length=2550)

    def __str__(self):
        return self.NameL


class cartTransactionMasters(models.Model):
    DateCreated = models.DateTimeField()


class categories(models.Model):
    MainCategoryId = models.ForeignKey(
        'self', on_delete=models.DO_NOTHING, default='null', db_column='MainCategoryId', null=True, db_constraint=False)
    NameA = models.TextField(max_length=2550, null=True)
    NameL = models.TextField(max_length=2550)
    Level = models.IntegerField()
    ImageUrl = models.TextField(max_length=2550, null=True)

    def __str__(self):
        return self.NameL


class countries(models.Model):
    NameA = models.TextField(max_length=2550, null=True)
    NameL = models.TextField(max_length=2550)
    Symbol = models.TextField(max_length=2550)

    def __str__(self):
        return self.NameL


class orderStatus(models.Model):
    Code = models.IntegerField()
    StatusNameA = models.TextField(max_length=2550, null=True)
    StatusNameL = models.TextField(max_length=2550)

    def __str__(self):
        return self.StatusNameL


class shippingAgents(models.Model):
    NameA = models.TextField(max_length=2550, null=True)
    NameL = models.TextField(max_length=2550)
    Address1 = models.TextField(max_length=2550)
    Address2 = models.TextField(max_length=2550, null=True)
    Phone = models.TextField(max_length=2550, null=True)
    Email = models.TextField(max_length=2550)
    Password = models.TextField(max_length=2550)
    PostCode = models.TextField(max_length=2550, null=True)

    def __str__(self):
        return self.NameL


class specificationValue(models.Model):
    Name = models.TextField(max_length=2550)

    def __str__(self):
        return self.Name


class specifications(models.Model):
    NameA = models.TextField(max_length=2550, null=True)
    NameL = models.TextField(max_length=2550)
    ShowInFilter = models.BooleanField(null=True)

    def __str__(self):
        return self.NameL


class transactionTypes(models.Model):
    Code = models.IntegerField()
    NameA = models.TextField(max_length=2550, null=True)
    NameL = models.TextField(max_length=2550)

    def __str__(self):
        return self.NameL


class users(models.Model):
    NameA = models.TextField(max_length=2550, null=True)
    NameL = models.TextField(max_length=2550)
    Email = models.TextField(max_length=2550)
    Password = models.TextField(max_length=2550)
    Address1 = models.TextField(max_length=2550, null=True)
    Address2 = models.TextField(max_length=2550, null=True)
    Phone = models.IntegerField(null=True)
    City = models.TextField(max_length=2550, null=True)

    def __str__(self):
        return self.NameL


class vendors(models.Model):
    NameA = models.TextField(max_length=2550, null=True)
    NameL = models.TextField(max_length=2550)
    Address1 = models.TextField(max_length=2550)
    Address2 = models.TextField(max_length=2550, null=True)
    Phone = models.TextField(max_length=2550, null=True)
    Email = models.TextField(max_length=2550)
    Password = models.TextField(max_length=2550)
    PostCode = models.TextField(max_length=2550, null=True)

    def __str__(self):
        return self.NameL


class products(models.Model):
    NameA = models.TextField(max_length=2550, null=True)
    NameL = models.TextField(max_length=2550)
    Image = models.ImageField(null=True, blank=True)
    Image2 = models.ImageField(null=True, blank=True)
    Image3 = models.ImageField(null=True, blank=True)
<<<<<<< HEAD
    Image4 = CloudinaryField('image', null=True, blank=True)
=======
    Image4 = CloudinaryField('image')
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6
    Description = models.TextField(max_length=2550, null=True)
    BrandId = models.ForeignKey(
        brands, on_delete=models.DO_NOTHING,  db_column='BrandId', db_constraint=False)
    CategoryId = models.ForeignKey(
        categories, on_delete=models.DO_NOTHING,  db_column='CategoryId', db_constraint=False)

    def __str__(self):
<<<<<<< HEAD
        return str(self.NameL)
=======
        return self.NameL
>>>>>>> 8bd5679f0915566d6e588b99e4c05e916e2e99f6


class vendorPriceLists(models.Model):
    VendorId = models.ForeignKey(
        vendors, on_delete=models.DO_NOTHING,  db_column='VendorId', db_constraint=False)
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING,  db_column='ProductId', db_constraint=False)
    CountryId = models.ForeignKey(
        countries, on_delete=models.DO_NOTHING,  db_column='CountryId', db_constraint=False)
    Price = models.FloatField()


class productSpecifications(models.Model):
    SpecificationName = models.TextField(max_length=2550)
    SpecificationValue = models.TextField(max_length=2550)
    ShowInFilter = models.BooleanField(null=True)
    CategoryId = models.ForeignKey(
        categories, on_delete=models.DO_NOTHING,  db_column='CategoryId', db_constraint=False)
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING,  db_column='ProductId', db_constraint=False)
    SpecificationId = models.ForeignKey(
        specifications, on_delete=models.DO_NOTHING,  db_column='SpecificationId', db_constraint=False)

    def __str__(self):
        return self.SpecificationName


class stores(models.Model):
    NameA = models.TextField(max_length=2550, null=True)
    NameL = models.TextField(max_length=2550)
    Email = models.TextField(max_length=2550)
    Address = models.TextField(max_length=2550, null=True)
    City = models.TextField(max_length=2550)
    Latitude = models.TextField(max_length=2550, null=True)
    Longitude = models.TextField(max_length=2550, null=True)
    CountryId = models.ForeignKey(
        countries, on_delete=models.DO_NOTHING,  db_column='CountryId', db_constraint=False)
    VendorId = models.ForeignKey(
        vendors, on_delete=models.DO_NOTHING,  db_column='VendorId', db_constraint=False)
    ShippingAgentId = models.ForeignKey(
        shippingAgents, on_delete=models.DO_NOTHING,  db_column='ShippingAgentId', db_constraint=False)

    def __str__(self):
        return self.NameL


class storeShippingAgents(models.Model):
    StoreId = models.ForeignKey(
        stores, on_delete=models.DO_NOTHING, db_column='StoreId', db_constraint=False)
    ShippingAgentId = models.ForeignKey(
        shippingAgents, on_delete=models.DO_NOTHING,  db_column='ShippingAgentId', db_constraint=False)


class shippingAgentUsers(models.Model):
    UserId = models.ForeignKey(
        users, on_delete=models.DO_NOTHING,  db_column='UserId', db_constraint=False)
    ShippingAgentId = models.ForeignKey(
        shippingAgents, on_delete=models.DO_NOTHING,  db_column='ShippingAgentId', db_constraint=False)


class inventoryBalances(models.Model):
    StoreId = models.ForeignKey(
        stores, on_delete=models.DO_NOTHING, db_column='StoreId', db_constraint=False)
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING,  db_column='ProductId', db_constraint=False)
    QuantityBalance = models.FloatField()


class inventoryDetails(models.Model):
    StoreId = models.ForeignKey(
        stores, on_delete=models.DO_NOTHING, db_column='StoreId', db_constraint=False)
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING,  db_column='ProductId', db_constraint=False)
    Quantity = models.FloatField(null=False)


class cartTransactions(models.Model):
    Quantity = models.FloatField()
    IsOrdered = models.IntegerField()
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING, db_column='ProductId', db_constraint=False)
    MasterId = models.ForeignKey(
        cartTransactionMasters, on_delete=models.DO_NOTHING, db_column='MasterId', db_constraint=False)
    StoreId = models.ForeignKey(
        stores, on_delete=models.DO_NOTHING, db_column='StoreId', db_constraint=False)


class orderMasters(models.Model):
    DateCreated = models.DateTimeField()
    ShippingAddress = models.TextField(max_length=2550, null=True)
    cartId = models.ForeignKey(
        cartTransactions, db_column='CartId', on_delete=models.DO_NOTHING, db_constraint=False)
    UserId = models.ForeignKey(
        users, on_delete=models.DO_NOTHING, db_column='UserId', db_constraint=False)
    OrderStatusId = models.ForeignKey(
        orderStatus, on_delete=models.DO_NOTHING, db_column='OrderStatusId', db_constraint=False)


class orders(models.Model):
    UnitPrice = models.FloatField()
    TotalPrice = models.FloatField()
    isDelivered = models.BooleanField()
    Latitude = models.TextField(max_length=2550, null=True)
    Longitude = models.TextField(max_length=2550,  null=True)
    Quantity = models.FloatField()
    DeliveredByUserId = models.ForeignKey(
        users, db_column='DeliveredByUserId', on_delete=models.DO_NOTHING, related_name='UserId', db_constraint=False, null=True)
    cartId = models.ForeignKey(
        cartTransactions, db_column='CartId', on_delete=models.DO_NOTHING, db_constraint=False)
    ProductId = models.ForeignKey(
        products, db_column='ProductId', on_delete=models.DO_NOTHING, db_constraint=False)
    StoreId = models.ForeignKey(
        stores, db_column='StoreId', on_delete=models.DO_NOTHING, db_constraint=False)
    MasterId = models.ForeignKey(
        cartTransactionMasters, db_column='MasterId', on_delete=models.DO_NOTHING, db_constraint=False)
    UserId = models.ForeignKey(
        users, db_column='UserId', on_delete=models.DO_NOTHING, db_constraint=False)
    ShippingAgentId = models.ForeignKey(
        shippingAgents,  db_column='ShippingAgentId', on_delete=models.DO_NOTHING, db_constraint=False, null=True)


class shippingDetails(models.Model):
    DeliveryNotes = models.TextField(max_length=2550, null=True)
    OrderId = models.ForeignKey(
        orders, on_delete=models.DO_NOTHING, db_column='OrderId', db_constraint=False)
    ShippingAgentId = models.ForeignKey(
        shippingAgents, on_delete=models.DO_NOTHING,  db_column='ShippingAgentId', db_constraint=False)

    def __str__(self):
        return self.DeliveryNotes


class productStoreRatings(models.Model):
    RatingId = models.IntegerField()
    ProductReview = models.TextField(max_length=2550, null=True)
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING,  db_column='ProductId', db_constraint=False)
    StoreId = models.ForeignKey(
        stores, on_delete=models.DO_NOTHING, db_column='StoreId', db_constraint=False)
    UserId = models.ForeignKey(
        users, on_delete=models.DO_NOTHING,  db_column='UserId', db_constraint=False)

    def __str__(self):
        return self.RatingId


class getHomeProducts(models.Model):
    StoreId = models.ForeignKey(
        stores, on_delete=models.DO_NOTHING, db_column='StoreId', db_constraint=False)
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING, db_column='ProductId', db_constraint=False)
    QuantityBalance = models.FloatField()
    ProductName = models.TextField(max_length=2550)
    StoreName = models.TextField(max_length=2550)
    Image = models.ImageField(null=True, blank=True)
    Image2 = models.ImageField(null=True, blank=True)
    Image3 = models.ImageField(null=True, blank=True)
    Image4 = models.ImageField(null=True, blank=True)
    Description = models.TextField(max_length=2550)
    Price = models.FloatField()
    Currency = models.TextField(max_length=2550)
    CategoryId = models.ForeignKey(
        categories, on_delete=models.DO_NOTHING, db_column='CategoryId', db_constraint=False)
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
        db_table = "gethomeproducts"


class specificationValueCount(models.Model):
    SpecificationId = models.IntegerField()
    SpecificationValue = models.TextField(max_length=2550)
    SpecificationCount = models.IntegerField()
    CategoryId = models.IntegerField()

    class Meta:
        managed = False
        db_table = "specificationvaluecount"


class starPercent(models.Model):
    ProductId = models.ForeignKey(
        products, on_delete=models.DO_NOTHING, db_column='ProductId', db_constraint=False)
    StoreId = models.ForeignKey(
        stores, on_delete=models.DO_NOTHING, db_column='StoreId', db_constraint=False)
    FiveStarsCount = models.FloatField()
    FourStarsCount = models.FloatField()
    ThreeStarsCount = models.FloatField()
    TwoStarsCount = models.FloatField()
    OneStarCount = models.FloatField()
    FiveStarsPercent = models.FloatField()
    FourStarsPercent = models.FloatField()
    ThreeStarsPercent = models.FloatField()
    TwoStarsPercent = models.FloatField()
    OneStarPercent = models.FloatField()
    averageRating = models.FloatField()
    OutOfFive = models.FloatField()
    allReviewsCount = models.IntegerField()

    class Meta:
        managed = False
        db_table = "getstarpercent"
