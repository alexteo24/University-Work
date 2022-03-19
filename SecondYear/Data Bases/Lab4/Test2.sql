create or alter view getBigWarehousesWithStorages as
	select WH.WarehouseID, WH.Location, SO.StorageID 
	from Warehouse WH inner join StorageOption SO on WH.WarehouseID = SO.WarehouseID
	where WH.Surface > 10
go

exec addToTables 'Warehouse'
exec addToTables 'StorageOption'

exec addToViews 'getBigWarehousesWithStorages'
exec addToTests 'test2'
exec connectTableToTest 'Warehouse', 'test2', 1500, 2
exec connectTableToTest 'StorageOption', 'test2', 2000, 3
exec connectViewToTest 'getBigWarehousesWithStorages', 'test2'

exec runTest 'test2'