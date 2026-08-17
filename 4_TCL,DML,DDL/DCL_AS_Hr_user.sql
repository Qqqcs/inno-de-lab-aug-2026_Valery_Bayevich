SELECT current_user; --Проверили что юзер - hr_user

SELECT * FROM Employees; --Тест 1 успешно

INSERT INTO employees (EmployeeID, FirstName, LastName, Department, Salary)
VALUES 
(666, 'BadBad', 'Hacker', 'Virus', '676767'); --Тест 2 (hr_user хотел добавить мошенника, но не смог) Ошибка: SQL Error [42501]: ERROR: permission denied for table employees

--Обновили права нашему hr_user

INSERT INTO employees (EmployeeID, FirstName, LastName, Department, Salary)
VALUES 
(666, 'Saul', 'Goodman', 'Lawyer', '700'); -- Тест 3 - INSERT сработал

UPDATE Employees 
	SET Salary = '900'
		WHERE FirstName = 'Saul'
		AND LastName = 'Goodman'; -- Тест 3 - UPDATE так же сработал 
		
SELECT * FROM Employees; -- Проверили изменения 

--**Не добавил Email Солу(((*

UPDATE Employees 
SET 
	Email = 'BetterCallSaul@Saul.Lawyer', 
	employeeid = 8
WHERE FirstName = 'Saul'
	AND LastName = 'Goodman'; --просто от себя для удовлетворения души (я же могу делать всякие безобидные прикольчики, да?...(Пока учусь и пока можно))