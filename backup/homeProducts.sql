CREATE VIEW GetHomeProducts AS

SELECT        invBalance.Id, invBalance.StoreId, pro.Id AS ProductId, invBalance.QuantityBalance, pro.NameL AS ProductName, store.NameL AS StoreName, pro.ImageUrl, pro.ImageUrl6, pro.ImageUrl7, pro.Description, vendorPrice.Price, 
                         Countries.Symbol AS Currency, pro.CategoryId, Vendors.NameL AS VendorName, (row_number() OVER (ORDER BY pro.Id) - 1) AS RowNum, (((row_number() OVER (ORDER BY pro.Id) - 1) / 8) + 1) AS PageNumber,
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 5) * 5) AS FiveStarsCount,
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 4) * 4) AS FourStarsCount,
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 3) * 3) AS ThreeStarsCount,
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 2) * 2) AS TwoStarsCount,
						 (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 1) AS OneStarsCount,
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId ) * 5) AS MaxTotalRating,
						 
						 ROUND(
							 ( ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 5) * 5)*1.0 + 
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 4) * 4)*1.0 +
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 3) * 3)*1.0 +
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 2) * 2)*1.0 +
						 (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 1)*1.0 ) /
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId ) * 5)*1.0
						 
						 ,2) * 100 AS finalProductRating,
						 
						 ROUND(((
							 ( ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 5) * 5)*1.0 + 
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 4) * 4)*1.0 +
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 3) * 3)*1.0 +
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 2) * 2)*1.0 +
						 (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 1)*1.0 ) /
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId ) * 5)*1.0
						 
						 ) * 100) / 100, 2) * 5 AS OutOfFivestring


						 
FROM           PyCommerce_inventorybalances AS invBalance LEFT OUTER JOIN
                        PyCommerce_products AS pro ON invBalance.ProductId = pro.Id LEFT OUTER JOIN
                        PyCommerce_stores AS store ON invBalance.StoreId = store.Id LEFT OUTER JOIN
                        PyCommerce_vendorpricelists AS vendorPrice ON vendorPrice.CountryId = store.CountryId AND vendorPrice.ProductId = pro.Id AND vendorPrice.VendorId = store.VendorId LEFT OUTER JOIN
                        PyCommerce_countries AS Countries ON Countries.Id = store.CountryId LEFT OUTER JOIN
                        PyCommerce_vendors AS Vendors ON Vendors.Id = store.VendorId