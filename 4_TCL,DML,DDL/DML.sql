SELECT * FROM Employees; --До

INSERT INTO employees (EmployeeID, FirstName, LastName, Department, Salary)
VALUES 
(6, 'Dmitry', 'Yarikov', 'Finance', '67000'),
(7, 'Alex', 'Yakidoyaki', 'HR', '420000'); -- Добавили двух новых сотрудников 

SELECT * FROM Employees; -- выбрали всех сотрудников

SELECT FirstName, LastName FROM employees
WHERE Department = 'IT'; -- Выбрали только Имя Фамилию из IT

UPDATE Employees
SET Salary = '65000'
WHERE FirstName = 'Alice'
	AND LastName = 'Smith'; -- Обновили зарплату Алисе

DELETE  FROM employees -- Удалили сотрудника Eve через id
WHERE FirstName = 'Eve'
	AND LastName = 'Davis';

SELECT * FROM Employees; -- Проверяем изменения 