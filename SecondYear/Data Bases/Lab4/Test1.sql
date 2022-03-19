create or alter view getTrucksOlder as
	select Age, count(*) as nrTrucks
	from Truck
	group by Age

go

exec addToTables 'Truck'
exec addToViews 'getTrucksOlder'
exec addToTests 'test1'
exec connectTableToTest 'Truck', 'test1', 2000, 1
exec connectViewToTest 'getTrucksOlder', 'test1'

exec runTest 'test1'

select * from Tests
select * from Tables
select * from Truck
