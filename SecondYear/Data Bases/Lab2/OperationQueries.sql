	--You must use:

--    arithmetic expressions in the SELECT clause in at least 3 queries;
--    conditions with AND, OR, NOT, and parentheses in the WHERE clause in at least 3 queries;  -
--    DISTINCT in at least 3 queries
--    ORDER BY in at least 2 queries
--    and TOP in at least 2 queries.


-- 2 queries with the union operation; use UNION [ALL] and OR;              -------------- DONE --------------     a)

-- Drivers and customers that live in floresti
SELECT 'Customer' AS Type, FirstName, LastName, PhoneNr
FROM Customer
WHERE HomeAddress = 'Floresti'
UNION
SELECT 'Driver' AS Type, FirstName, LastName, PhoneNr
From Driver
WHERE HomeAddress = 'Floresti'

-- Top 3 storages which are almost empty or their expiration date is less than 7 days away
SELECT TOP 3 StorageID 
FROM StorageOption
WHERE DATEDIFF(day, '2021-11-05', ExpirationDate) < 7 OR StoredAmount < Capacity/10

-- 2 queries with the intersection operation; use INTERSECT and IN;               -------------- DONE --------------      b)


-- Drivers which have orders to deliver
SELECT FirstName, LastName
FROM Driver
WHERE DriverID IN(
	SELECT DriverID--, FirstName, LastName
	FROM Driver
	INTERSECT
	SELECT DriverID
	FROM Delivery)

-- Customers currently expecting an order which costs at least 100
SELECT FirstName, LastName, PhoneNr
FROM Customer
WHERE CustomerID IN(
	SELECT CustomerID
	FROM Orders
	Where Status = 'Not delivered' AND Cost >= 100)

-- 2 queries with the difference operation; use EXCEPT and NOT IN;              -------------- DONE --------------     c)

-- Drivers with no work to do
SELECT FirstName, LastName
FROM Driver
WHERE DriverID IN(
	SELECT DriverID --, FirstName, LastName
	FROM Driver
	EXCEPT
	SELECT DriverID
	FROM Delivery)


-- Farmers with no products currently in stock
SELECT FarmerID, FirstName, LastName
FROM Farmer
WHERE FarmerID NOT IN(
	Select FarmerID
	From ProductFromFarmer)

-- 4 queries with INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN (one query per operator);              -------------- DONE --------------     d)
-- one query will join at least 3 tables, while another one will join at least two many-to-many relationships;

-- Display the warehouse id in which each products are stored
-- SELECT P.ProductID, S.WarehouseID FROM ProductStored P inner join StorageOption S on S.StorageID = P.StorageID

-- Name of farmers whose products are in an order
SELECT DISTINCT F.FirstName, F.LastName from Farmer F 
	inner join ProductFromFarmer PFF on F.FarmerID = PFF.FarmerID 
	inner join Product P on PFF.ProductID = P.ProductID
	inner join ProductPartOfOrder PPOF on P.PricePerKg = PPOF.ProductID

-- Display the name, id of all the products, and the quantity of the products that are part of an order
SELECT P.Name, P.ProductID, PPOF.Quantity FROM ProductPartOfOrder PPOF right join Product P on P.ProductID = PPOF.ProductID

-- Displays all the customers in the database and the cost and status of their orders, if they have any
SELECT C.FirstName, C.LastName, O.Cost, O.Status FROM Customer C left join Orders O on C.CustomerID = O.CustomerID ORDER BY O.Cost

-- Displaying products and information about there they are being stored if that is the case
SELECT SO.StorageID, SO.WarehouseID, PS.Quantity, P.ProductID, P.Name FROM StorageOption SO full join ProductStored PS on PS.StorageID = SO.StorageID full join Product P on PS.ProductID = P.ProductID

--SELECT 

-- 2 queries with the IN operator and a subquery in the WHERE clause;              -------------- DONE --------------     e)
-- in at least one case, the subquery should include a subquery in its own WHERE clause;

-- List of products provided by at least 2 farmers

SELECT DISTINCT Name
FROM Product
WHERE ProductID IN(
	SELECT PFF.ProductID
	FROM ProductFromFarmer PFF
	GROUP BY PFF.ProductID
	HAVING COUNT(*) > 1)

-- List of products which are currently part of an order that was not delivered
SELECT Name, Type, PricePerKg
FROM Product
WHERE ProductID IN(
	SELECT ProductID
	FROM ProductPartOfOrder
	WHERE OrderID IN(
		SElECT OrderID
		FROM Orders
		WHERE Status = 'Not delivered'))

-- 2 queries with the EXISTS operator and a subquery in the WHERE clause;              -------------- DONE --------------     f)

-- Show trucks that are currently being used by at least 1 driver
SELECT T.LicensePlate, T.Age
FROM Truck T
WHERE EXISTS(
	SELECT *
	FROM Driver
	WHERE LicensePlate = T.LicensePlate)

-- Seeing the customer ID FName and LName of the customers which still have undelivered orders
SELECT CustomerID, FirstName, LastName
FROM Customer
WHERE EXISTS(
	SELECT ExpectedDeliveryDate 
	FROM Orders 
	WHERE Customer.CustomerID = Orders.CustomerID AND Orders.Status='Not delivered')

-- 2 queries with a subquery in the FROM clause;              -------------- DONE --------------     g)

-- Displaying the name of the first 3 products, which take more than 80% of their designed storage option and will expire in 6 months, and their price lowered by 2
SELECT TOP 3 P.Name, P.PricePerKg - 2 as DecreasedPrice  -- arithmetic in select  -- using top
FROM (
	SELECT P.Name, P.PricePerKg FROM StorageOption SO inner join ProductStored PS on PS.StorageID = SO.StorageID and SO.StoredAmount > 0.8*SO.Capacity AND
	DATEDIFF(MONTH, '2021-11-05', SO.ExpirationDate) < 6 inner join Product P on P.ProductID = PS.ProductID
) P
ORDER BY DecreasedPrice  -- uusing order BY

-- Displaying the incrased delivery cost for the deliveries outside of Cluj-Napoca
SELECT C.FirstName, C.LastName, C.HomeAddress, C.Cost + 15 as increasedCost -- arithmetic in select
FROM (SELECT C.FirstName, C.LastName, C.HomeAddress, O.Cost FROM Customer C inner join Orders O on C.CustomerID = O.CustomerID AND C.HomeAddress <> 'Cluj-Napoca' AND
	O.Status = 'Not delivered'
) C
ORDER BY increasedCost DESC -- uusing order BY

-- 4 queries with the GROUP BY clause, 3 of which also contain the HAVING clause;              -------------- DONE --------------     h)

-- 2 of the latter will also have a subquery in the HAVING clause; use the aggregation operators: COUNT, SUM, AVG, MIN, MAX; \

 -- IDs of the farmers which have provided at least 3 different products
SELECT PFF.FarmerID, COUNT(*) as products
FROM ProductFromFarmer PFF
group by PFF.FarmerID
having count(*) > 2


 -- IDs of the farmer along with the number of products provided
SELECT FarmerID, count(*) as nrProducts
FROM ProductFromFarmer
group by FarmerID

 -- The names of the farmers which have provided more products than the average of all the farmers
SELECT F.FirstName, F.LastName
FROM Farmer F
WHERE F.FarmerID IN(
	SELECT PFF.FarmerID
	FROM ProductFromFarmer PFF
	GROUP BY PFF.FarmerID
	HAVING Count(PFF.FarmerID) > (
		SELECT AVG(nrProducts) as average
		FROM(
			SELECT PFF.FarmerID, Count(PFF.ProductID) as nrProducts
			FROM ProductFromFarmer PFF
			group by PFF.FarmerID)F
	)
)

 -- The names of the farmer which have provided a quantity of products bigger than the average
SELECT F.FirstName, F.LastName
FROM Farmer F
WHERE F.FarmerID IN(
	SELECT PFF.FarmerID
	FROM ProductFromFarmer PFF
	GROUP BY PFF.FarmerID
	HAVING AVG(PFF.Quantity) > (
		SELECT AVG(PFF.Quantity) as average
		FROM ProductFromFarmer PFF)
)
-- 4 queries using ANY and ALL to introduce a subquery in the WHERE clause (2 queries per operator);              -------------- DONE --------------     i)
-- rewrite 2 of them with aggregation operators, and the other 2 with IN / [NOT] IN.


-- Farms with a surface larger than all farms in Cluj-Napoca
SELECT F.FarmID, F.Surface, F.Location
FROM Farm F
WHERE F.Surface > ALL(
	SELECT F2.Surface
	FROM Farm F2
	where F2.Location = 'Cluj-Napoca')

-- Farms with a surface larger than all farms in Cluj-Napoca(aggregation)
SELECT F.FarmID, F.Surface, F.Location
FROM Farm F
WHERE F.Surface > (
	SELECT MAX(F2.Surface)
	FROM Farm F2
	WHERE F2.Location = 'Cluj-Napoca')

-- Drivers with more experinece at the company than at least one drivers from Cluj-Napoca
SELECT D.HomeAddress, D.FirstName, D.LastName, D.Experience
FROM Driver D
WHERE D.Experience > ANY(
	SELECT D2.Experience
	FROM Driver D2
	WHERE D2.HomeAddress = 'Cluj-Napoca')

-- Drivers with more experinece at the company than at least one drivers from Cluj-Napoca(aggregation)
SELECT D.HomeAddress, D.FirstName, D.LastName, D.Experience
FROM Driver D
WHERE D.Experience >(
	SELECT MIN(D2.Experience)
	FROM Driver D2
	WHERE D2.HomeAddress = 'Cluj-Napoca')


-- Seeing the oldest 3 cars running on deisel
SELECT TOP 3 T.LicensePlate, T.NrKilometers
FROM Truck T
WHERE T.FuelType <> ANY(
	SELECT T1.FuelType
	FROM Truck T1
	WHERE T1.FuelType = 'Petrol'
	)
ORDER BY T.Age DESC

-- Seeing the oldest 3 cars running on deisel	
SELECT TOP 3 T.LicensePlate, T.NrKilometers  -- using top
FROM Truck T
WHERE T.LicensePlate IN(
	SELECT T1.LicensePlate
	FROM Truck T1
	WHERE T1.FuelType = 'Diesel'
	)
ORDER BY T.Age DESC

-- products that have not been supplied by any farmer with a price increased by 30%
SELECT P.Name, P.PricePerKg + 0.3*P.PricePerKg as pretCriza -- arithmetic in select
FROM Product P
WHERE P.ProductID NOT IN(
	SELECT PS.ProductID
	FROM ProductStored PS)
ORDER BY pretCriza DESC

-- products that have not been supplied by any farmer with a price increased by 30%
SELECT P.Name, P.PricePerKg + 0.3*P.PricePerKg as pretCriza -- arithmetic in select
FROM Product P
WHERE P.ProductID = ANY(
	SELECT P.ProductID
	FROM Product P
	WHERE P.ProductID NOT IN(
		SELECT DISTINCT PS.ProductID FROM ProductStored PS inner join ProductFromFarmer PPF on PS.ProductID = PPF.ProductID))
ORDER BY pretCriza DESC
--SELECT P.Name
--FROM Product P
--WHERE P.ProductID <> ALL(
--	SELECT PS.ProductID
--	FROM ProductStored PS)


--Valid questions:

--Seeing the customers who ordered the most

--Seeing the products whose expiration dates are due soon

--Seeing all farmers which supply a nr of products/more than the average nr of supplied products