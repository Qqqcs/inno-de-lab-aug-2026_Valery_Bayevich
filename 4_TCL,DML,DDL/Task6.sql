SELECT p.ProjectName
FROM Projects p
JOIN EmployeeProjects ep
	ON p.ProjectID = ep.ProjectID
JOIN Employees e
	ON e.EmployeeID = ep.EmployeeID
WHERE e.FirstName = 'Bob'
	AND e.lastName = 'Johnson'
	AND ep.Hoursworked > 150; --Нашли имена всех проектов где Боб работал больше 150 часов

UPDATE Projects p
SET Budget = Budget * 1.10
WHERE EXISTS (
	SELECT 1
	FROM employeeProjects ep
	JOIN Employees e
		ON e.employeeID = ep.EmployeeID 
	WHERE ep.ProjectID = p.ProjectID
		AND e.Department = 'IT' --Оно ничего не обновит, тк рабочие из IT перешли в Senior IT 

);

UPDATE Projects p
SET Budget = Budget * 1.10
WHERE EXISTS (
	SELECT 1
	FROM employeeProjects ep
	JOIN Employees e
		ON e.employeeID = ep.EmployeeID 
	WHERE ep.ProjectID = p.ProjectID
		AND e.Department = 'Senior IT' --То же самое, но увеличит бюджет всех проектов

);


UPDATE Projects 
SET EndDate = StartDate + INTERVAL '1 year' --Дату конца проекта поставили на год позже начала 
WHERE EndDate IS NULL;

SELECT * FROM Projects; --Проверить

BEGIN;

WITH new_employee AS (
	INSERT INTO Employees (FirstName, LastName, Department, Salary)
	VALUES ('Gordon', 'Freeman', 'Designer', 90200) --Создаем нового сотрудника
	RETURNING EmployeeID
);

INSERT INTO employeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT
	new_employee.EmployeeID,
	p.projectID,
	80
FROM new_employee
JOIN Projects p
	ON p.ProjectName = 'Website Redesign';

COMMIT; 

SELECT * FROM employeeProjects;