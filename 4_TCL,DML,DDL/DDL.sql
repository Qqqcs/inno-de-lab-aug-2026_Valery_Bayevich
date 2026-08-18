CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
); --Создали новую таблицу Departments

ALTER TABLE Employees
	ADD COLUMN Email VARCHAR(100); -- Добавили столбец Email

SELECT * FROM Employees;

UPDATE Employees 
	SET Email = 'BobiJohn@gmail.com'
		WHERE FirstName = 'Bob'
		AND LastName = 'Johnson';
UPDATE Employees 
	SET Email = 'CharlieBrown34591@mail.ru'
		WHERE FirstName = 'Charlie'
		AND LastName = 'Brown';
UPDATE Employees 
	SET Email = 'PrinceDaniel39@gmail.com'
		WHERE FirstName = 'Diana'
		AND LastName = 'Prince';
UPDATE Employees 
	SET Email = 'AgentSmith1999@gmail.com'
		WHERE FirstName = 'Alice'
		AND LastName = 'Smith';
UPDATE Employees 
	SET Email = 'ToliDmitry_ToliYarik@gmail.com'
		WHERE FirstName = 'Dmitry'
		AND LastName = 'Yarikov';
UPDATE Employees 
	SET Email = 'IgralVContryNoTeperRabotayu@mail.ru'
		WHERE FirstName = 'Alex'
		AND LastName = 'Yakidoyaki'; --Добавили почту для всех сотрудников (Наверное лучше было бы сделать это через кейс, но я не уверен)
		
ALTER TABLE Employees ADD CONSTRAINT UQ_Employees_Email UNIQUE (Email); -- Сделали ограничение столбцу Email 

SELECT * FROM Departments;
ALTER TABLE Departments RENAME COLUMN Location TO OfficeLocation; --Переименовали столбец Location на OfficeLocation в таблице Departments
SELECT * FROM Departments;