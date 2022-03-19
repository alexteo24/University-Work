drop table Tc
drop table Tb
drop table Ta

create table Ta (
    aid int primary key,
    a2 int unique,
    x int
)

create table Tb (
    bid int primary key,
    b2 int,
    x int
)

create table Tc (
    cid int primary key,
    aid int references Ta(aid),
    bid int references Tb(bid)
)

go
create or alter procedure insertIntoTa(@rows int) as
    declare @max int
    set @max = 1
    while @rows > 0 begin
        insert into Ta values (@rows, @max, @rows%865) -- FLOOR(RAND() * (@rows - 1) + @rows)
        set @rows = @rows-1
        set @max = @max + 1
    end

go
create or alter procedure insertIntoTb(@rows int) as
    while @rows > 0 begin
        insert into Tb values (@rows, @rows%735, @rows%665)  -- FLOOR(RAND() * (@rows - 1) + @rows)
        set @rows = @rows-1
    end

go
create or alter procedure insertIntoTc(@rows int) as
    declare @aid int
    declare @bid int
    while @rows > 0 begin
        set @aid = (select top 1 aid from Ta order by NEWID())
        set @bid = (select top 1 bid from Tb order by NEWID())
        insert into Tc values (@rows, @aid, @bid)
        set @rows = @rows-1
    end


exec insertIntoTa 15000
exec insertIntoTb 15000
exec insertIntoTc 5000


create nonclustered index indexTa on Ta(x)
drop index indexTa on Ta
    
select * from Ta order by aid -- clustered index scan  cost: 0.04
select * from Ta where aid = 190 -- clustered index seek cost: 0.003
select x from Ta order by x -- non custered index scan cost: 0.03
select a2 from Ta where a2 = 7646 -- non clustered index seek cost: 0.003
select x from Ta where a2 = 9879 -- key lookup cost: 0.006

select * from Tb where b2 = 590 -- Clustered Index Scan cost: 0.04 without index

create nonclustered index indexTb on Tb(b2) include (bid, x)
drop index indexTb on Tb

select * from Tb where b2 = 590 -- Clustered Index Scan cost: 0.03 with index

go
create or alter view view1 as
    select top 1000 T1.x, T2.b2
    from Tc T3 join Ta T1 on T3.aid = T1.aid join Tb T2 on T3.bid = T2.bid
    where T2.b2 > 500 and T1.x < 600

go

select * from view1 -- cost with indexes: 0.29
					-- cost without indexes: 0.36
