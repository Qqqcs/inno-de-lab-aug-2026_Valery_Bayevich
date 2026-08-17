CREATE USER hr_user WITH PASSWORD '228337';

CREATE ROLE homework4_user_Grant;
GRANT SELECT ON Employees TO homework4_user_Grant;

GRANT homework4_user_Grant TO hr_user; --Создали нового пользователя. 1й вариант как в лекции

--*****************************************ИЛИ****************************************************--

CREATE USER hr_user WITH PASSWORD '228337';

GRANT SELECT ON Employees TO hr_user; --2й вариант, но наверное менее практичный тк выдается роль только одному юзеру 

--Провели тесты

GRANT INSERT, UPDATE ON Employees TO hr_user; -- Добавили новые права