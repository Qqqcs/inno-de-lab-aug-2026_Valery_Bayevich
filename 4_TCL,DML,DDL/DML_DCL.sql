SELECT * FROM Employees

UPDATE Employees
SET Salary = Salary * 1.10
WHERE Department = 'HR'; -- Подняли зарплаты на 10% сотрудникам с HR

SELECT * FROM Employees;

UPDATE Employees
	SET department = 'Senior IT'
	WHERE salary > 70000; --Обновили отдел ребятам с большой зарплатой

SELECT * FROM EmployeeProjects

DELETE FROM Employees e
	WHERE NOT EXISTS (
		SELECT 1
		FROM EmployeeProjects ep
		WHERE ep.EmployeeID = e.EmployeeID
	); --Удалили сотрудников, не назначенных ни на один проект
	
	
SELECT * FROM Projects; 

BEGIN; --начало транзакции

INSERT INTO Projects (projectid,projectname, budget, startdate, enddate)
VALUES (4, 'Half-Life 3', 1000000, Current_date, NULL); --добавили проект

INSERT INTO EmployeeProjects (employeeid, projectid, hoursworked)  
VALUES (1, 4, 42),
	   (3, 4, 350);--Закинули на проект сотрудников 

COMMIT; --конец транзакции

SELECT * FROM Projects;
SELECT * FROM EmployeeProjects;



