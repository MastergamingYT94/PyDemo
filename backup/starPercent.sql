CREATE VIEW GetStarPercent AS

SELECT     (row_number() OVER ()) AS id , pro.Id AS ProductId, invBalance.StoreId,
                         
						 (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 5) AS FiveStarsCount,
						 (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 4) AS FourStarsCount,
						 (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 3) AS ThreeStarsCount,
						 (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 2) AS TwoStarsCount,
						 (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 1) AS OneStarsCount,
						 
						 ROUND(((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 5) * 1.0 / 
						   (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId)) * 100, 2) AS FiveStarPercent,
						 ROUND(((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 4) * 1.0 / 
							(SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId)) * 100, 2) AS FourStarPercent,
						 ROUND(((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 3) * 1.0 / 
						   (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId)) * 100, 2) AS ThreeStarPercent,
						 ROUND(((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 2) * 1.0 / 
						   (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId)) * 100, 2) AS TwoStarPercent,
						 ROUND(((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 1) * 1.0 / 
						   (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId)) * 100, 2) AS OneStarPercent,
			
						 
						 ROUND((( ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 5) *5) *1.0 +
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 4) *4) *1.0 +
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 3) *3) *1.0 +
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 2) *2) *1.0 +
						 (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 1) *1.0 ) /
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId) * 5) *100), 2) AS averageRating,
						 
						 
						  ROUND( ((( ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 5) *5) *1.0 +
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 4) *4) *1.0 +
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 3) *3) *1.0 +
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 2) *2) *1.0 +
						 (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId and  rating.RatingId = 1) *1.0 ) /
						 ((SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId) * 5) *100) / 100) *5, 1) AS OutOfFive,
						 
						 (SELECT COUNT (*) FROM PyCommerce_productstoreratings AS rating WHERE rating.ProductId = invBalance.ProductId and rating.StoreId = invBalance.StoreId) AS allReviewsCount

		


						 
FROM           PyCommerce_inventorybalances AS invBalance LEFT OUTER JOIN
                        PyCommerce_products AS pro ON invBalance.ProductId = pro.Id LEFT OUTER JOIN
                        PyCommerce_stores AS store ON invBalance.StoreId = store.Id LEFT OUTER JOIN
                        PyCommerce_vendorpricelists AS vendorPrice ON vendorPrice.CountryId = store.CountryId AND vendorPrice.ProductId = pro.Id AND vendorPrice.VendorId = store.VendorId LEFT OUTER JOIN
                        PyCommerce_countries AS Countries ON Countries.Id = store.CountryId LEFT OUTER JOIN
                        PyCommerce_vendors AS Vendors ON Vendors.Id = store.VendorId