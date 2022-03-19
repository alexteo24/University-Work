--Write SQL scripts that:
--a. modify the type of a column;     ---- DONE ----
--b. add / remove a column;     ---- DONE ----
--c. add / remove a DEFAULT constraint;     ---- DONE ----
--d. add / remove a primary key;     ---- DONE ----
--e. add / remove a candidate key;     ---- DONE ----
--f. add / remove a foreign key;     ---- DONE ----
--g. create / drop a table.       ---- DONE ----

--For each of the scripts above, write another one that reverts the operation. 
--Place each script in a stored procedure. Use a simple, intuitive naming convention.

--Create a new table that holds the current version of the database schema. 
--Simplifying assumption: the version is an integer number.

--Write a stored procedure that receives as a parameter a version number 
--and brings the database to that version

CREATE TABLE VersionTable (
	version INT
)

INSERT INTO VersionTable VALUES (0) -- 0 being the initial version of tha database

SELECT * FROM VersionTable

-- a) modify column type
GO
CREATE OR ALTER PROCEDURE setEmployeeExperienceFromWarehouseEmployeeTinyint as
	ALTER TABLE warehouseEmployee ALTER COLUMN experience tinyint

-- undo

GO
CREATE OR ALTER PROCEDURE setEmployeeExperienceFromWarehouseEmployeeInt as
	ALTER TABLE warehouseEmployee ALTER COLUMN experience INT

-- b) add/remove a column

GO
CREATE OR ALTER PROCEDURE addSalaryToWarehouseEmployee AS
	ALTER TABLE warehouseEmployee ADD Salary INT

-- undo

GO
CREATE OR ALTER PROCEDURE removeSalaryFromWarehouseEmployee AS
	ALTER TABLE warehouseEmployee DROP COLUMN Salary

-- c) add/remove default constraint

GO
CREATE OR ALTER PROCEDURE addDefaultToExperienceFromWarehouseEmployee AS
	ALTER TABLE warehouseEmployee ADD CONSTRAINT defaultExperience default(0) FOR Experience

-- undo

GO
CREATE OR ALTER PROCEDURE removeDefaultFromExperienceFromWarehouseEmployee AS
	ALTER TABLE warehouseEmployee DROP CONSTRAINT defaultExperience

-- d) add/remove a primary key

GO
CREATE OR ALTER PROCEDURE removePrimaryKeyEmployee AS
	ALTER TABLE warehouseEmployee
		drop constraint EMPLOYEE_PRIMARY_KEY

-- undo

GO
CREATE OR ALTER PROCEDURE addPrimaryKeyEmployee AS
	ALTER TABLE warehouseEmployee
		add constraint EMPLOYEE_PRIMARY_KEY PRIMARY KEY (employeeID)

-- e) add/remove a candidate key

GO
CREATE OR ALTER PROCEDURE addCandidateKeyEmployee AS
	ALTER TABLE warehouseEmployee ADD CONSTRAINT EMPLOYEE_CANDIDATE_KEY_1 UNIQUE(phoneNr, homeAddres)

-- undo

GO
CREATE OR ALTER PROCEDURE removeCandidateKeyEmployee AS
	ALTER TABLE warehouseEmployee DROP CONSTRAINT EMPLOYEE_CANDIDATE_KEY_1

-- f) add/remove a foreign key

GO
CREATE OR ALTER PROCEDURE addForeignKeyEmployee AS
	ALTER TABLE warehouseEmployee ADD CONSTRAINT EMPLOYEE_FOREIGN_KEY FOREIGN KEY(WarehouseID) REFERENCES Warehouse(WarehouseID)

-- undo

GO
CREATE OR ALTER PROCEDURE removeForeignKeyEmployee AS
	ALTER TABLE warehouseEmployee DROP CONSTRAINT EMPLOYEE_FOREIGN_KEY

--g) add/remove a table

GO
CREATE OR ALTER PROCEDURE addEmployee as
	CREATE TABLE warehouseEmployee(
		firstName VARCHAR(50),
		lastName VARCHAR(50),
		phoneNr VARCHAR(10),
		homeAddres VARCHAR(50),
		employeeID INT,
		experience INT,
		WarehouseID INT,
		constraint EMPLOYEE_PRIMARY_KEY PRIMARY KEY(employeeID)
	)
-- undo

GO
CREATE OR ALTER PROCEDURE dropEmployee as
	DROP TABLE warehouseEmployee

GO

DROP TABLE ProcedureTable
CREATE TABLE ProcedureTable (
	fromVersion INT,
	toVersion INT,
	PRIMARY KEY(fromVersion, toVersion),
	storedProcedure VARCHAR(MAX)
)

GO
INSERT INTO ProcedureTable VALUES (0, 1, 'addEmployee')
INSERT INTO ProcedureTable VALUES (1, 0, 'dropEmployee')
INSERT INTO ProcedureTable VALUES (1, 2, 'setEmployeeExperienceFromWarehouseEmployeeTinyint')
INSERT INTO ProcedureTable VALUES (2, 1, 'setEmployeeExperienceFromWarehouseEmployeeInt')
INSERT INTO ProcedureTable VALUES (2, 3, 'addSalaryToWarehouseEmployee')
INSERT INTO ProcedureTable VALUES (3, 2, 'removeSalaryFromWarehouseEmployee')
INSERT INTO ProcedureTable VALUES (3, 4, 'addDefaultToExperienceFromWarehouseEmployee')
INSERT INTO ProcedureTable VALUES (4, 3, 'removeDefaultFromExperienceFromWarehouseEmployee')
INSERT INTO ProcedureTable VALUES (4, 5, 'removePrimaryKeyEmployee')
INSERT INTO ProcedureTable VALUES (5, 4, 'addPrimaryKeyEmployee')
INSERT INTO ProcedureTable VALUES (5, 6, 'addCandidateKeyEmployee')
INSERT INTO ProcedureTable VALUES (6, 5, 'removeCandidateKeyEmployee')
INSERT INTO ProcedureTable VALUES (6, 7, 'addForeignKeyEmployee')
INSERT INTO ProcedureTable VALUES (7, 6, 'removeForeignKeyEmployee')

GO
CREATE OR ALTER PROCEDURE goToVersion(@newVersion int) AS
	DECLARE @current INT
	DECLARE @var VARCHAR(MAX)
	SELECT @current=version FROM VersionTable

	if @newVersion > (SELECT max(toVersion) FROM ProcedureTable)
		raiserror ('Bad version', 10, 1)

	WHILE @current > @newVersion
	BEGIN
		SELECT @var = storedProcedure from ProcedureTable WHERE fromVersion = @current and toVersion = @current-1
		exec(@var)
		SET @current = @current - 1
	END

	WHILE @current < @newVersion
	BEGIN
	select @var = storedProcedure from ProcedureTable where fromVersion = @current and toVersion = @current+1
        exec (@var)
        set @current = @current+1
    end

	update versionTable set version=@newVersion

SELECT * FROM VersionTable
EXECUTE goToVersion 0
SELECT * FROM ProcedureTable
SELECT * FROM VersionTable
update versionTable set version=0
SELECT * FROM warehouseEmployee
EXEC('dropEmployee')
