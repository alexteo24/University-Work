DROP TABLE ProductStored
DROP TABLE StorageOption
DROP TABLE Warehouse
DROP TABLE Delivery
DROP TABLE ProductPartOfOrder
DROP TABLE Orders
DROP TABLE DrivesOnRoute
DROP TABLE ProductFromFarmer
DROP TABLE Farmer
DROP TABLE Product
DROP TABLE Customer
DROP TABLE Driver
DROP TABLE Route
DROP TABLE Farm
DROP TABLE Truck

CREATE TABLE Farm ( -- 1 Farm can have multiple farmers => 1:n
FarmID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
Surface INT,
Location VARCHAR(max),
);

CREATE TABLE Farmer ( -- 1 farmer cand work only at one farm
FarmerID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
FirstName VARCHAR(max),
LastName VARCHAR(max),
PhoneNr VARCHAR(50),
FarmmmmmmID INT FOREIGN KEY REFERENCES Farm(FarmID) ON UPDATE CASCADE ON DELETE CASCADE,
);

CREATE TABLE Product (
ProductID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
Name VARCHAR(max),
Type VARCHAR(max),
PricePerKg INT,
);

CREATE TABLE ProductFromFarmer ( -- 1 product can be from multiple farmers and a farmer may have multiple products => m:n
ProductID INT FOREIGN KEY REFERENCES Product(ProductID) ON UPDATE CASCADE ON DELETE CASCADE,
FarmerID INT FOREIGN KEY REFERENCES Farmer(FarmerID) ON UPDATE CASCADE ON DELETE CASCADE,
Quantity INT,
PRIMARY KEY (ProductID, FarmerID),
);

CREATE TABLE Warehouse(
WarehouseID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
Surface INT,
Location VARCHAR(max),
);

CREATE TABLE Customer( -- 1 customer can be expecting multiple deliveries => 1:n
CustomerID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
FirstName VARCHAR(max),
LastName VARCHAR(max),
HomeAddress VARCHAR(max),
PhoneNr VARCHAR(50),
);

CREATE TABLE Truck(
LicensePlate VARCHAR(50) NOT NULL PRIMARY KEY,
FuelType VARCHAR(50),
Age INT,
NrKilometers INT,
);

CREATE TABLE Route(
RouteID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
City VARCHAR(max),
Area VARCHAR(max),
);

CREATE TABLE Driver( -- 1 driver will have to do multiple deliveries, but 1 delivery cand be associated only to 1 driver => 1:n
DriverID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
FirstName VARCHAR(max),
LastName VARCHAR(max),
HomeAddress VARCHAR(max),
PhoneNr VARCHAR(50),
Experience INT,
LicensePlate VARCHAR(50) FOREIGN KEY REFERENCES Truck(LicensePlate) ON UPDATE CASCADE ON DELETE CASCADE,
);

CREATE TABLE DrivesOnRoute(
DriverID INT FOREIGN KEY REFERENCES Driver(DriverID) ON UPDATE CASCADE ON DELETE CASCADE,
RouteID INT FOREIGN KEY REFERENCES Route(RouteID) ON UPDATE CASCADE ON DELETE CASCADE,
NrStops INT,
PRIMARY KEY (DriverID, RouteID),
);

CREATE TABLE Orders(
OrderID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
CustomerID INT FOREIGN KEY REFERENCES Customer(CustomerID) ON UPDATE CASCADE ON DELETE CASCADE,
OrderDate DATE,
ExpectedDeliveryDate DATE,
Cost INT,
Status VARCHAR(20),
);

CREATE TABLE Delivery( -- 1 delivery can go only to 1 specific customer
OrderID INT FOREIGN KEY REFERENCES Orders(OrderID) ON DELETE CASCADE ON UPDATE CASCADE,
DriverID INT FOREIGN KEY REFERENCES Driver(DriverID) ON UPDATE CASCADE ON DELETE CASCADE,
PRIMARY KEY(OrderID, DriverID)
);

CREATE TABLE ProductPartOfOrder(
OrderID INT FOREIGN KEY REFERENCES Orders(OrderID) ON DELETE CASCADE ON UPDATE CASCADE,
ProductID INT FOREIGN KEY REFERENCES Product(ProductID) ON DELETE CASCADE ON UPDATE CASCADE,
PRIMARY KEY (OrderID, ProductID),
Quantity INT,
);

CREATE TABLE StorageOption(
StorageID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
WarehouseID INT NOT NULL FOREIGN KEY REFERENCES Warehouse(WarehouseID) ON UPDATE CASCADE ON DELETE CASCADE,
ExpirationDate DATE,
Type VARCHAR(20),
StoredAmount INT,
Capacity INT,
);

CREATE TABLE ProductStored( -- in a warehouse we can store multiple products, and a product (eg. apples) can be stored in different warehouses =>m:n
StorageID INT FOREIGN KEY REFERENCES StorageOption(StorageID) ON UPDATE CASCADE ON DELETE CASCADE,
ProductID INT FOREIGN KEY REFERENCES Product(ProductID) ON UPDATE CASCADE ON DELETE CASCADE,
Quantity INT,
PRIMARY KEY(StorageID, ProductID),
);