create or alter procedure addToTables(@tableName varchar(50)) as
	if @tableName in (select Name from Tables) begin
		print 'The table is already in Tables'
		return
	end
	if @tableName not in(select TABLE_NAME from INFORMATION_SCHEMA.TABLES) begin
		print 'The table does not exist in the database'
		return
	end
	insert into Tables (Name) values (@tableName)


GO
create or alter procedure addToViews(@viewName varchar(50)) as
	if @viewName in (select Name from Views) begin
        print 'The view is already in Views'
        return
    end
    if @viewName not in (select TABLE_NAME from INFORMATION_SCHEMA.VIEWS) begin
        print 'The view does not exist in the database'
        return
    end
    insert into Views (Name) values (@viewName)


GO
create or alter procedure addToTests (@testName varchar(50)) as
    if @testName in (select Name from Tests) begin
        print 'Test already present in Tests'
        return
    end
    insert into Tests (Name) values (@testName)

GO
create or alter procedure connectTableToTest(@tableName varchar(50), @testName varchar(50), @rows int, @pos int) as
	if @tableName not in (select Name from Tables)
	begin
		print 'Table does not exist'
		return
	end

	if @testName not in (select Name from Tests)
	begin
		print 'Test does not exist'
		return
	end
	if exists
		(select *
		from TestTables T1 join Tests T2 on T1.TestID = T2.TestID
		where T2.Name = @testName and Position = @pos
		)
	begin
		print 'Position provided conflicts with previous positions'
		return
	end
	insert into TestTables (TestID, TableID, NoOfRows, Position) 
	values ((select Tests.TestID from Tests where Name = @testName),
			(select Tables.TableID from Tables where Name = @tableName),
			@rows, @pos)

GO
create or alter procedure connectViewToTest (@viewName varchar(50), @testName varchar(50)) as
	if @viewName not in (select Name from Views)
	begin
		print 'View does not exist in Views'
		return
	end
	if @testName not in (select Name from Tests)
	begin
		print 'Test oes not exist in Tests'
		return
	end
	insert into TestViews (TestID, ViewID) 
	values ((select Tests.TestID from Tests where Name = @testName),
			(select Views.ViewID from Views where Name = @viewName))

GO
create or alter procedure runTest (@testName varchar(50)) as
	if @testName not in (select Name from Tests)
		begin
			print 'That test does not exist in Tests'
			return
		end
	declare @command varchar(100)
    declare @testStartTime datetime2
    declare @startTime datetime2
    declare @endTime datetime2
	declare @table varchar(50)
    declare @rows int
    declare @pos int
    declare @view varchar(50)
    declare @testId int
    select @testId=TestID from Tests where Name=@testName
    declare @testRunId int
    set @testRunId = (select max(TestRunID)+1 from TestRuns)
    if @testRunId is null
        set @testRunId = 0
    declare tableCursor cursor scroll for
        select T1.Name, T2.NoOfRows, T2.Position
        from Tables T1 join TestTables T2 on T1.TableID = T2.TableID
        where T2.TestID = @testId
        order by T2.Position
    declare viewCursor cursor for
        select V.Name
        from Views V join TestViews TV on V.ViewID = TV.ViewID
        where TV.TestID = @testId

    set @testStartTime = sysdatetime()
    open tableCursor
    fetch last from tableCursor into @table, @rows, @pos
    while @@FETCH_STATUS = 0 begin
        exec uspDeleteFromTable @tableName = @table
        fetch prior from tableCursor into @table, @rows, @pos
    end
    close tableCursor

    open tableCursor
    SET IDENTITY_INSERT TestRuns ON
    insert into TestRuns (TestRunID, Description, StartAt)values (@testRunId, 'Tests results for: ' + @testName, @testStartTime)
    SET IDENTITY_INSERT TestRuns OFF
    fetch tableCursor into @table, @rows, @pos
    while @@FETCH_STATUS = 0 begin
        set @startTime = sysdatetime()
		exec uspInsertTable @tableName = @table, @nrRows = @rows
        set @endTime = sysdatetime()
        insert into TestRunTables (TestRunID, TableId, StartAt, EndAt) values (@testRunId, (select TableID from Tables where Name=@table), @startTime, @endTime)
        fetch tableCursor into @table, @rows, @pos
    end
    close tableCursor
    deallocate tableCursor

    open viewCursor
    fetch viewCursor into @view
    while @@FETCH_STATUS = 0 begin
        set @command = 'select * from ' + @view
        set @startTime = sysdatetime()
        exec (@command)
        set @endTime = sysdatetime()
        insert into TestRunViews (TestRunID, ViewID, StartAt, EndAt) values (@testRunId, (select ViewID from Views where Name=@view), @startTime, @endTime)
        fetch viewCursor into @view
    end
    close viewCursor
    deallocate viewCursor

    update TestRuns
    set EndAt=sysdatetime()
    where TestRunID = @testRunId

declare testCursor CURSOR
for select Name from Tests

open testCursor
declare @tName as varchar(20)

fetch next from testCursor into @tName
while @@FETCH_STATUS = 0
	BEGIN
		exec runTest @tName
		fetch next from testCursor into @tName
	END
close testCursor
deallocate testCursor

select * from Tests
select * from TestRuns
select * from TestRunTables
select * from TestRunViews