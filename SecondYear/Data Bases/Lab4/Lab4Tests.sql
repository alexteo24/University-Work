GO
create or alter procedure generateRandomString @stringValue varchar(20) OUTPUT
AS
declare @length as INT
declare @charPool as VARCHAR(55)
declare @charPoolLength as INT
    set @charPool = 'abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
    set @charPoolLength = Len(@charPool)
    set @length = FLOOR(RAND() * (10 - 1) + 10)
    set @stringValue = ''
    while @length > 0
        BEGIN
            set @stringValue = @stringValue + SUBSTRING(@charPool, CONVERT(INT, RAND() * @charPoolLength) + 1, 1)
            set @length = @length - 1
        END
GO
create or alter procedure uspDeleteFromTable(@tableName VARCHAR(50)) AS
BEGIN
    exec ('delete from ' + @tableName)
    if exists(select *
              from sys.identity_columns
              where object_id = (select object_id from sys.tables where name = @tableName))
        BEGIN
            dbcc checkident (@tableName, reseed, 0)
        END
END
GO
create or alter procedure uspInsertTable(@tableName VARCHAR(50), @nrRows INT) AS
BEGIN
    if exists(select * from sys.tables o where type = 'U' and o.name = @tableName)
        BEGIN
            -- getting column names and associated data types
            declare data_cursor SCROLL CURSOR
                for
                select p.name, p.DATA_TYPE
                from (
                         select c.name, c.column_id, i.DATA_TYPE
                         from sys.objects o
                                  inner join sys.columns c on o.object_id = c.object_id
                                  inner join INFORMATION_SCHEMA.COLUMNS i
                                             on i.TABLE_NAME = @tableName and i.COLUMN_NAME = c.name
                         where type = 'U'
                           and o.name = @tableName) p
                order by p.column_id

            -- constructing the insert querry
            declare @insert as VARCHAR(max)

            -- name and data type for columns
            declare @columnName as VARCHAR(20)
            declare @dataType as VARCHAR(10)
            declare @intValue as INT
            declare @stringValue as VARCHAR(50)
            declare @checkPKQuerry as NVARCHAR(2000)
			declare @hasPk as int


            -- opening cursor
            open data_cursor

            while @nrRows > 0
                BEGIN
					set @hasPk = 0
                    set @insert = 'INSERT INTO ' + @tableName + ' VALUES('
					set @checkPKQuerry = ''
					set @checkPKQuerry = N'select @outputPK=count(*) from ' + @tableName + ' where '
                    fetch first from data_cursor into @columnName, @dataType;
                    while @@FETCH_STATUS = 0 -- getting data types from the previous select
                        BEGIN
							--select @insert as insertForColumn, @columnName as currentColumn
                            if COLUMNPROPERTY(OBJECT_ID(@tableName), @columnName, 'IsIdentity') = 0
                                BEGIN
									--select 'got in the identity for hte column ' + @columnName as WasInNonIdentity, @insert as insertNow
                                    -- if column is not identity, must be added


                                    -- TODO TREBUIE LUCRAT MAI DEGRABA PE BAZA ID ULUI DECAT A NUMELUI PENTRU CA ID UL E UNIQ, NUMELE NU

									declare @referencedTable as varchar(50)--
									declare @referencedColumn as varchar(50)--
									set @referencedTable = ''
									set @referencedColumn = ''
                                    select @referencedColumn = KCU.COLUMN_NAME, @referencedTable =  KCU.TABLE_NAME
									from INFORMATION_SCHEMA.CONSTRAINT_TABLE_USAGE TU
									inner join INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS RC on TU.CONSTRAINT_NAME = RC.CONSTRAINT_NAME
									inner join INFORMATION_SCHEMA.KEY_COLUMN_USAGE KCU on RC.UNIQUE_CONSTRAINT_NAME = KCU.CONSTRAINT_NAME
									inner join INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE CCU on CCU.CONSTRAINT_NAME = RC.CONSTRAINT_NAME
									where CCU.COLUMN_NAME = @columnName and @tableName = CCU.TABLE_NAME
									if (len(@referencedTable) > 0 and len(@referencedColumn) > 0)
                                        -- current column is a foreign key
                                        BEGIN
											
                                            -- selecting referenced table name
                                            --declare @referencedTable as varchar(50)
                                            /*select @referencedTable = [name]
                                            from sys.tables t
                                            where t.object_id = (
                                                select referenced_object_id
                                                from sys.foreign_keys fk
                                                where fk.name = (
                                                    select CONSTRAINT_NAME
                                                    from INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
                                                    where @columnName = COLUMN_NAME
                                                      and TABLE_NAME = @tableName
                                                      and CONSTRAINT_NAME like 'FK%')
                                            )*/




                                            if @dataType = 'int'
                                                BEGIN
                                                    declare @getMaxIdQuery as NVARCHAR(100)
                                                    set @getMaxIdQuery =
                                                                N'select @maxId = MAX(' + @referencedColumn + ') from ' +
                                                                @referencedTable
                                                    --select @getMaxIdQuery
                                                    declare @maxId as INT
                                                    exec sp_executesql @getMaxIdQuery, N'@maxId int output', @maxId OUTPUT
                                                    set @intValue = FLOOR(RAND() * (@maxId) + 1)
                                                    set @insert = @insert + cast(@intValue as Varchar(10)) + ','
													--select @insert as insertForNonIdentityFK, @columnName as onColumn, @getMaxIdQuery as executedQuery, @maxId as queryOutput, @intValue as insertValue
                                                END
                                            else
                                                if @dataType = 'varchar'
                                                    BEGIN
                                                        /*declare @tableName as varchar(20)
                                                        set @tableName = 'Truck'
                                                        declare @columnName as varchar(20)
                                                        set @columnName = 'LicensePlate'
                                                        declare @stringValue as varchar(50)*/
                                                        declare @getStringQuery as NVARCHAR(200)
                                                        set @getStringQuery =
                                                                    N'select top 1 @stringValue = [' + @referencedColumn +
                                                                    ']' + ' from ' + @referencedTable + ' t where t.' +
                                                                    @referencedColumn + ' = t.' + @referencedColumn +
                                                                    ' order by newid()'
                                                        exec sp_executesql @getStringQuery,
                                                             N'@stringValue varchar(50) output', @stringValue output
                                                        set @insert = @insert + ''''+ @stringValue + ''','
														--select @insert as insertForNonIdentityFK, @columnName as onColumn, @getStringQuery as executedQuery, @stringValue as queryOutput, @stringValue as insertValue
                                                    END
											
                                        END
                                    else -- not a foreign key
                                        BEGIN
                                            if @dataType = 'int'
                                                BEGIN
                                                    set @intValue = FLOOR(RAND() * (21 - 1) + 1)
                                                    set @insert = @insert + cast(@intValue as Varchar(10)) + ','
													--select @insert as insertForNonIdentityNonFK, @columnName as onColumn, @intValue as insertValue
                                                END
                                            else
                                                if @dataType = 'varchar'
                                                    BEGIN
                                                        EXEC generateRandomString @stringValue output
                                                        set @insert = @insert + '''' + @stringValue + '''' + ','
														--select @insert as insertForNonIdentityNonFK, @columnName as onColumn, @stringValue as insertValue
                                                    END
                                                else
                                                    BEGIN
                                                        set @insert = @insert + 'NULL' + ','
                                                    END
											
                                        END
                                    -- must check for multicolumn primary keys/primary keys
									if exists(select *
                                      from INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
                                      where TABLE_NAME = @tableName
                                        and @columnName = COLUMN_NAME
                                        and CONSTRAINT_NAME like 'PK%')
										BEGIN
											set @hasPk = 1
											if @dataType = 'varchar'
												BEGIN
													set @checkPKQuerry = @checkPKQuerry + @columnName + '=''' + @stringValue + ''' and '
												END
											if @dataType = 'int'
												BEGIN
													set @checkPKQuerry = @checkPKQuerry + @columnName + '=' +
																		 cast(@intValue as VARCHAR(10)) + ' and '
												END
										--select @insert as insertForNonIdentityPK, @columnName as onColumn, @checkPKQuerry as currentCheckPKQuery
										END
										
                                END
                            /*if exists(select *
                                      from INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
                                      where TABLE_NAME = @tableName
                                        and @columnName = COLUMN_NAME
                                        and CONSTRAINT_NAME like 'PK%')
                                BEGIN
                                    if @dataType = 'varchar'
                                        BEGIN
                                            set @checkPKQuerry = @checkPKQuerry + @columnName + '=' + @stringValue + ' and '
                                        END
                                    if @dataType = 'int'
                                        BEGIN
                                            set @checkPKQuerry = @checkPKQuerry + @columnName + '=' +
                                                                 cast(@intValue as VARCHAR(10)) + ' and '
                                        END
                                END*/
                            FETCH NEXT FROM data_cursor into @columnName, @dataType
                        END
					--select @insert as finalInsert
                    if @hasPk = 1
                        BEGIN
							set @checkPKQuerry = left(@checkPKQuerry, LEN(@checkPKQuerry) - 4)
                            declare @outputPK as int
                            exec sp_executesql @checkPKQuerry, N'@outputPK int output', @outputPK output
                            if @outputPK = NULL or @outputPK = 0
                                BEGIN
                                    set @insert = left(@insert, LEN(@insert) - 1) + ')'
                                    EXEC (@insert)
                                    set @nrRows = @nrRows - 1
                                END
                        END
                    else
                        BEGIN
							--select @checkPKQuerry as checkQuery, @insert as insertQuery
                            set @insert = left(@insert, LEN(@insert) - 1) + ')'
                            EXEC (@insert)
                            set @nrRows = @nrRows - 1
                        END
                END
            close data_cursor
            deallocate data_cursor
        END
    else
        BEGIN
            print 'Table does not exist'
            return
        END
END
select *
from Product

-- testing things
select o.name, c.name
from sys.objects o
         inner join sys.columns c on o.object_id = c.object_id
where type = 'U'
order by o.object_id, c.column_id

select *
from sys.objects o
         inner join sys.columns c on o.object_id = c.object_id
where type = 'U'

select *
from INFORMATION_SCHEMA.COLUMNS

select *
from sys.columns

select *
from sys.tables
WHERE type = 'U'

select *
from sys.foreign_keys

select *
from INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE c
where c.CONSTRAINT_NAME like 'PK%'

DECLARE
    @id AS INT = 9999, @name as VARCHAR(50) = 'Red', @type as VARCHAR(50) = 'Color', @price AS INT = 10, @tableNam as VARCHAR(50) = 'Product'

DECLARE
    @proc AS VARCHAR(max) = 'INSERT INTO ' + @tableNam + ' VALUES(' + '''' + @name + '''' + ',' + '''' + @type + '''' +
                            ','

    SET @id = 10
    SET @proc = @proc + cast(@id as VARCHAR(10)) + ')'

SELECT @proc

    EXEC (@proc)

select COLUMN_NAME, TABLE_NAME
from INFORMATION_SCHEMA.COLUMNS
where COLUMNPROPERTY(object_id(TABLE_SCHEMA + '.' + TABLE_NAME), COLUMN_NAME, 'IsIdentity') = 1
order by TABLE_NAME

SELECT COLUMNPROPERTY(OBJECT_ID('Product'), 'ProductID', 'IsIdentity')

SELECT RAND() * (10 - 1) + 1


    EXEC uspInsertTable @tableName = 'Farm', @nrRows = 10

select *
from Farm

delete
from Farm
where FarmID >= 4

select *
from sys.tables
where object_id = 788249913

select *
from sys.foreign_keys
select *
from sys.tables
where type = 'U'
select *
from INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
select *
from sys.identity_columns

declare @checkPKQuerry as NVARCHAR(200)
declare @outputShit as INT

    set @checkPKQuerry =
                N'select @outputShit=count(*) from ' + 'Product' + ' where Type=''Fruit'' or Type=''Vegetable'''

    exec sp_executesql @checkPKQuerry, N'@outputShit INT output', @outputShit output

select @outputShit
exec uspInsertTable @tableName = 'Product', @nrRows = 100
exec uspInsertTable @tableName = 'Warehouse', @nrRows = 100
exec uspInsertTable @tableName = 'StorageOption', @nrRows = 100
exec uspInsertTable @tableName = 'ProductStored', @nrRows = 100
exec uspInsertTable @tableName = 'Farm', @nrRows = 100
exec uspInsertTable @tableName = 'Farmer', @nrRows = 100
exec uspInsertTable @tableName = 'ProductFromFarmer', @nrRows = 100
exec uspInsertTable @tableName = 'Customer', @nrRows = 100
exec uspInsertTable @tableName = 'Orders', @nrRows = 100
exec uspInsertTable @tableName = 'Truck', @nrRows = 100
exec uspInsertTable @tableName = 'Route', @nrRows = 100
exec uspInsertTable @tableName = 'Driver', @nrRows = 100
exec uspInsertTable @tableName = 'Delivery', @nrRows = 100
exec uspInsertTable @tableName = 'DrivesOnRoute', @nrRows = 100

select *
from Product
exec uspDeleteFromTable @tableName = 'Product'
select *
from Warehouse
exec uspDeleteFromTable @tableName = 'Warehouse'
select *
from StorageOption
exec uspDeleteFromTable @tableName = 'StorageOption'
select *
from ProductStored
exec uspDeleteFromTable @tableName = 'ProductStored'
select *
from Farm
exec uspDeleteFromTable @tableName = 'Farm'
select *
from Farmer
exec uspDeleteFromTable @tableName = 'Farmer'
select *
from ProductFromFarmer
exec uspDeleteFromTable @tableName = 'ProductFromFarmer'
select *
from Customer
exec uspDeleteFromTable @tableName = 'Customer'
select *
from Orders
exec uspDeleteFromTable @tableName = 'Orders'
select *
from Truck
exec uspDeleteFromTable @tableName = 'Truck'
select *
from Driver
exec uspDeleteFromTable @tableName = 'Driver'
select *
from Delivery
exec uspDeleteFromTable @tableName = 'Delivery'
select *
from DrivesOnRoute
exec uspDeleteFromTable @tableName = 'DrivesOnRoute'

select TU.TABLE_NAME, RC.CONSTRAINT_NAME, RC.UNIQUE_CONSTRAINT_NAME, KCU.COLUMN_NAME as referencedColumn, CCU.COLUMN_NAME as currentColumn, KCU.TABLE_NAME as referencedTable
from INFORMATION_SCHEMA.CONSTRAINT_TABLE_USAGE TU
inner join INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS RC on TU.CONSTRAINT_NAME = RC.CONSTRAINT_NAME
inner join INFORMATION_SCHEMA.KEY_COLUMN_USAGE KCU on RC.UNIQUE_CONSTRAINT_NAME = KCU.CONSTRAINT_NAME
inner join INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE CCU on CCU.CONSTRAINT_NAME = RC.CONSTRAINT_NAME
where CCU.COLUMN_NAME = 'ProductID' and 'Product' = CCU.TABLE_NAME

select * from INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
select * from INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS