INSERT INTO Customer(FirstName, LastName, HomeAddress, PhoneNr)
VALUES('Rosa', 'Rees', 'Floresti', '0756295731'), 
	('Miley', 'Bryan', 'Cluj-Napoca', '0735827592'),
	('Elvira', 'Donald', 'Floresti' ,'0768275712'),
	('Oran', 'Floyd', 'Cluj-Napoca', '0749276632'),
	('Hamza', 'Craig' , 'Cluj-Napoca', '0775922756'),
	('George', 'Bush' , 'Cluj-Napoca', '0775022756'),
	('Zeorze', 'Buzz' , 'Cluj-Napoca', '0775022756')

INSERT INTO Truck(LicensePlate, FuelType, Age, NrKilometers)
VALUES('CJ-01-HTD', 'Diesel', 6, 350000),
	('CJ-05-HTD', 'Diesel', 5, 295000),
	('CJ-07-HTD', 'Diesel', 7, 301000),
	('CJ-09-HTD', 'Diesel', 3, 156000),
	('CJ-11-HTD', 'Petrol', 1, 70000),
	('CJ-12-HTD', 'Petrol', 0, 0),
	('CJ-16-HTD', 'Diesel', 4, 220000)

INSERT INTO Route(City, Area)
VALUES('Cluj-Napoca', 'Marasti'),
	('Cluj-Napoca', 'Gheorgheni'),
	('Cluj-Napoca', 'Centru'),
	('Cluj-Napoca', 'Intre Lacuri'),
	('Cluj-Napoca', 'Floresti'),
	('Cluj-Napoca', 'Centru'),
	('Cluj-Napoca', 'Centru')

INSERT INTO Farm(Surface, Location)
VALUES (150, 'Cluj-Napoca'),
	(175, 'Cluj-Napoca'),
	(300, 'Floresti')

INSERT INTO Farmer(FirstName, LastName, PhoneNr, FarmID)
VALUES ('Nathan', 'Pearson', '0762967339', 1),
	('Arman', 'Bond', '0727020146', 2),
	('Orson', 'Bain', '0750295710',1),
	('Emanuel', 'Rankin', '0762815029',2),
	('Oran', 'Buck', '0731086933', 3),
	('Derek', 'Logan', '0773672910', 2),
	('Jody', 'Green', '0759206910', 3),
	('Carrie', 'Plummer', '0762091059', 3),
	('Emily', 'Stark', '0769376021', 1),
	('Heidi', 'Rocha', '0755628615', 3)

INSERT INTO Driver(FirstName, LastName, HomeAddress, PhoneNr, Experience, LicensePlate)
VALUES ('Leopold', 'Duggan', 'Floresti', '0745495737', 2, 'CJ-01-HTD'),
	('Solomon', 'Wilkerson', 'Cluj-Napoca', '0728315015', 3, 'CJ-11-HTD'),
	('Lianne', 'Ayala', 'Cluj-Napoca', '0722510039', 1, 'CJ-07-HTD'),
	('Iona', 'Mcloughlin', 'Cluj-Napoca', '0762609709', 2, 'CJ-05-HTD'),
	('Derrick', 'Huber', 'Cluj-Napoca', '0722503704', 3, 'CJ-09-HTD'),
	('Rosa', 'Irwin', 'Zalau', '0728213330', 5, 'CJ-07-HTD'),
	('Duncan', 'Bishop', 'Floresti', '0744500719', 4, 'CJ-01-HTD')

INSERT INTO Warehouse(Surface, Location)
VALUES (1000, 'Cluj-Napoca'),
	(2000, 'Floresti'),
	(1500, 'Cluj-Napoca')

INSERT INTO StorageOption(WarehouseID, ExpirationDate, Type, StoredAmount, Capacity)
VALUES (1, '2022-01-23', 'Egg Fridge', 130, 150), --
	(2, '2022-01-17', 'Milk Fridge', 230, 300), --
	(1, '2021-11-07', 'Fruit Crate', 60, 125), --
	(2, '2021-11-08', 'Fruit Crate', 120, 175), --
	(3, '2021-12-10', 'Diary Frigde', 60, 125), --
	(1, '2022-02-27', 'Meat Freezer', 210, 220), --
	(2, '2022-02-25', 'Fridge', 150, 250), --
	(3, '2021-12-31', 'Vegetable Crate',175, 200), --
	(2, '2022-05-23', 'Meat Freezer', 25, 300), --
	(3, '2022-04-19', 'Vegetable Crate', 75, 250), -- 
	(2, '2021-11-08', 'Fruit Crate', 90, 115), --
	(1, '2021-12-31', 'Vegetable Crate', 75, 200) --


INSERT INTO Product(Name, Type, PricePerKg)
VALUES ('Red Apple', 'Fruit', 5),
	('Green Apple', 'Fruit', 9),
	('Strawberry', 'Fruit', 20),
	('Milk', 'Dairy', 10),
	('Cheese', 'Dairy', 50),
	('Eggs', 'Eggs', 10),
	('Chicken', 'Meat', 19),
	('Pork', 'Meat', 25),
	('Beef', 'Meat', 22),
	('Sausage', 'Meat', 15),
	('Salami', 'Meat', 23),
	('Tomato', 'Vegetable', 8),
	('Cucumber', 'Vegetable', 5),
	('Eggplant', 'Vegetable', 7),
	('Lettuce', 'Vegetable', 9),
	('Salad', 'Vegetable', 9), 
	('Onion', 'Vegetable', 6),
	('Lamb', 'Meat', 50)


INSERT INTO ProductFromFarmer(ProductID, FarmerID, Quantity)
VALUES (1, 2, 90), -- done
	(2, 4, 75), -- done
	(3, 9, 60), -- done
	(4, 1, 200), -- done
	(5, 3, 60), -- done
	(6, 2, 100), -- done
	(7, 3, 55), -- done
	(8, 1, 70), -- done
	(9, 9, 85), -- done
	(10, 9, 50), -- done
	(11, 1, 100), -- done
	(12, 4, 120), -- done
	(13, 7, 75), -- done
	(14, 8, 45), -- done
	(15, 10, 30), -- done
	(2, 2, 45), -- done
	(7, 1, 25), -- done
	(12, 10, 55), -- done
	(4, 2, 50), -- done
	(6, 3, 30) -- done

INSERT INTO ProductStored(StorageID, ProductID, Quantity)
VALUES (1, 6, 130),
	(2, 4, 230),
	(3, 3, 60),
	(4, 2, 120),
	(11, 1, 00),
	(5, 5, 60),
	(6, 7, 55),
	(6, 8, 70),
	(6, 9, 85),
	(7, 10, 50),
	(7, 11, 100),
	(9, 7, 25),
	(8, 12, 175),
	(12, 13, 75),
	(10, 14, 45),
	(10, 15, 30)

INSERT INTO DrivesOnRoute(DriverID, RouteID, NrStops)
VALUES (1, 5, 10),
	(2, 1, 6),
	(3, 7, 13),
	(4, 6, 11),
	(5, 2, 9),
	(6, 4, 8),
	(7, 3, 15),
	(7, 5, 16)


INSERT INTO Orders(CustomerID, OrderDate, ExpectedDeliveryDate, Cost, Status)
VALUES (1, '2021-11-05', '2021-11-01', 53, 'Not delivered'),
	(5, '2021-11-04', '2021-11-06', 38, 'Not delivered'),
	(2, '2021-11-01', '2021-11-03', 38, 'Delivered'),
	(5, '2021-11-05', '2021-11-07', 40, 'Not delivered'),
	(4, '2021-11-10', '2021-11-11', 100, 'Not delivered'),
	(3, '2021-11-09', '2021-11-10', 125, 'Not delivered'),
	(1, '2021-11-07', '2021-11-09', 70, 'Not delivered'),
	(1, '2021-11-07', '2021-11-09', 75, 'Cancelled')

	
INSERT INTO Delivery(OrderID, DriverID)
VALUES (1, 5),
	(2, 3),
	(6, 1),
	(7, 2),
	(4, 2),
	(3, 4),
	(5, 6)--,    INSERT VIOLATING CONSTRAINTS
	--(10, 6)

INSERT INTO ProductPartOfOrder(OrderID, ProductID, Quantity)
VALUES (1, 10, 2),
	(7, 4, 2),
	(2, 12, 3),
	(6, 8, 5),
	(4, 3, 2),
	(1, 11, 1),
	(3, 7, 2),
	(5, 5, 2),
	(2, 13, 2),
	(7, 6, 5)


update Truck
SET NrKilometers = 300000
WHERE Age BETWEEN 4 and 10  -- usage of between

update Orders
SET COST = 9/10 * COST
WHERE DATEDIFF(MONTH, '2021-11-9', ExpectedDeliveryDate) > 1  -- usage of >

update Product
SET PricePerKg = PricePerKg + 1
WHERE PricePerKg is not null  -- usage of is not null

delete Customer where Customer.HomeAddress in ('Zalau', 'Turda')  -- usage of in

delete FROM Orders where Orders.Status = 'Cancelled' or Orders.Status = 'Delivered'  -- usage of or

delete FROM Product where Product.ProductID = 16  -- usage of =

delete FROM Customer where Customer.FirstName LIKE 'z%'  -- usage of like, deletes customers whose fnames start with a z

update Warehouse  -- usage of <=
set Surface = Surface + 100
where WarehouseID <= 2
