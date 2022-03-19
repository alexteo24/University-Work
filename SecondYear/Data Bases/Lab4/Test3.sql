create or alter view getProductsSuppliedByFarmers as
select PricePerKg, count(P.ProductID) as nrProducts
from Product p
inner join ProductFromFarmer PPF on P.ProductID= PPF.ProductID
inner join Farmer F on PPF.FarmerID = F.FarmerID
group by P.PricePerKg
go

exec addToTables 'Product'
exec addToTables 'Farm'
exec addToTables 'Farmer'
exec addToTables 'ProductFromFarmer'

exec addToTests 'test3'
exec addToViews 'getProductsSuppliedByFarmers'
exec connectTableToTest 'Product', 'test3', 2000, 1
exec connectTableToTest 'Farm', 'test3', 2000, 2
exec connectTableToTest 'Farmer', 'test3', 1500, 3
exec connectTableToTest 'ProductFromFarmer', 'test3', 1500, 4
exec connectViewToTest 'getProductsSuppliedByFarmers', 'test3'

exec runTest 'test3'