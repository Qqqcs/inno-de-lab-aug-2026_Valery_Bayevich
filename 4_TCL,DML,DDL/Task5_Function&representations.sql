CREATE FUNCTION CalculateAnnualBonus(
employee_id INT,
salary decimal
);
RETURNS decimal
LANGUAGE PLpgSQL
AS $$
BEGIN
		RETURN salary * 0.10;
END;
$$; --Создали функцию которая принимает employee_id и salary и возвращает 10% от зп


SELECT EmployeeID, FirstName, LastName, Salary, CalculateAnnualBonus(EmployeeId, Salary) AS AnnualBonus
FROM Employees; --Смотрим на бонус для каждого сотрудника 

CREATE VIEW IT_Department_View AS 
SELECT EmployeeID, FirstName, LastName, Salary
FROM employees
WHERE Department = 'IT'; --Сделал IT но из-за высокой зарплаты и перевода всех сотрудников из IT в SeniorIT оно ничего не показало

SELECT * FROM IT_Department_View; --Ничего не показало, таблица пустая

CREATE VIEW IT_Department_View2 AS -- вторая вьюшка, которая что-то покажет
SELECT EmployeeID, FirstName, LastName, Salary
FROM employees
WHERE Department = 'Senior IT'; --Тут вместо IT - стоит Senior IT 

SELECT * FROM IT_Department_View2; --Тк раньше мы перевели сотрудников с IT в Senior IT (Как на зло у всех была зарплата выше 70000), пришлось выкручиваться