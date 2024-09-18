-- 1.3 Create a database named “UnivDB” with 2 data files and 1 log file.

CREATE DATABASE UnivDB 

ON 

  (NAME = UnivDB_Data1, 

   FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\UnivDB_Data1.mdf',

   SIZE = 10MB, 

   MAXSIZE = 100MB, 

   FILEGROWTH = 20%), 

  (NAME = UnivDB_Data2, 

   FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\UnivDB_Data2.ndf',

   SIZE = 10MB, 

   MAXSIZE = 100MB, 

   FILEGROWTH = 20%)

LOG ON 

  (NAME = UnivDB_Log, 

   FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\UnivDB_Log.ldf',

   SIZE = 10MB, 

   MAXSIZE = 100MB, 

   FILEGROWTH = 20%)

go

-- 2.1 Create a database named “mydb1” without specifying any file information.

CREATE DATABASE mydb1 

go

--2.2 Create a database named “mydb2” with 2 data files and 1 log file.

CREATE DATABASE mydb2

ON 

  (NAME = mydb2_Data1, 

   FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\mydb2_Data1.mdf',

   SIZE = 10MB, 

   MAXSIZE = 100MB, 

   FILEGROWTH = 20%), 

  (NAME = mydb2_Data2, 

   FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\mydb2_Data2.ndf',

   SIZE = 10MB, 

   MAXSIZE = 100MB, 

   FILEGROWTH = 20%)

LOG ON 

  (NAME = mydb2_Log, 

   FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\mydb2_Log.ldf',

   SIZE = 10MB, 

   MAXSIZE = 100MB, 

   FILEGROWTH = 20%) 

go

-- 2.3 Add a new data file into the database “mydb2” with initial size of 5MB.

ALTER DATABASE mydb2 

ADD FILE (

    NAME = mydb2_Data_02, 

   FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\mydb2_Data_02.ndf',

    SIZE = 5MB, 

    FILEGROWTH = 20%

);

go



-- 2.4 Change the growth rate for the newly added data file in “mydb2” to 30%.

ALTER DATABASE mydb2 

MODIFY FILE (

    NAME = mydb2_Data_02, 

    FILEGROWTH = 30%

);

go

-- 2.5 Change the name of “mydb2” to “mydb3”.

ALTER DATABASE mydb2 

MODIFY NAME = mydb3;

go

-- 2.6 Drop the database "mydb1".

DROP DATABASE mydb1;

go

-- 2.7 Create two tables in database “mydb3” for departments and students, and set up their references.

USE mydb3;

go

CREATE TABLE Departments (

    DeptID INT PRIMARY KEY,

    DeptName VARCHAR(50),

);

go

CREATE TABLE Students (

    StudentID INT PRIMARY KEY,

    StudentName VARCHAR(50),

    DeptID INT,

    FOREIGN KEY (DeptID) REFERENCES Departments (DeptID)

);

go

-- 2.8 Add a new column in table of departments to record their office locations.

ALTER TABLE Departments 

ADD OfficeLocation VARCHAR(50);

go

-- 2.10 Drop the table of students.

DROP TABLE Students;

go

--Create database

CREATE DATABASE EMS;

go

--3) Insert data for an Employee Management System (EMS)

--Use database

USE EMS;

go

--Create DEPT table

CREATE TABLE DEPT (

    DEPTNO INT PRIMARY KEY,

    DNAME VARCHAR(14),

    LOC VARCHAR(13)

);

go

--Insert data into DEPT table

INSERT INTO DEPT (DEPTNO, DNAME, LOC) VALUES

(10, 'ACCOUNTING', 'NEW YORK'),

(20, 'RESEARCH', 'DALLAS'),

(30, 'SALES', 'CHICAGO'),

(40, 'OPERATIONS', 'BOSTON');

go

--Create SALGRADE table

CREATE TABLE SALGRADE (

    GRADE INT PRIMARY KEY,

    LOSAL INT,

    HISAL INT

);

go

--Insert data into SALGRADE table

INSERT INTO SALGRADE (GRADE, LOSAL, HISAL) VALUES

(1, 700, 1200),

(2, 1201, 1400),

(3, 1401, 2000),

(4, 2001, 3000),

(5, 3001, 9999);

go

--Create EMP table

CREATE TABLE EMP (

    EMPNO INT PRIMARY KEY,

    ENAME VARCHAR(10),

    JOB VARCHAR(9),

    MGR INT,

    HIREDATE DATE,

    SAL INT,

    COMM INT,

    DEPTNO INT,

    FOREIGN KEY (DEPTNO) REFERENCES DEPT (DEPTNO),

    FOREIGN KEY (MGR) REFERENCES EMP (EMPNO)

);

go

--Insert data into EMP table

INSERT INTO EMP (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO) VALUES

(7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800, NULL, 20),

(7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20', 1600, 300, 30),

(7521, 'WARD', 'SALESMAN', 7698, '1981-02-22', 1250, 500, 30),

(7655, 'JONES', 'MANAGER', 7839, '1981-04-02', 2975, NULL, 20),

(7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28', 1250, 1400, 30),

(7698, 'BLAKE', 'MANAGER', 7839, '1991-05-01', 2850, NULL, 30),

(7782, 'CLARK', 'MANAGER', 7839, '1981-06-09', 2450, NULL, 10),

(7788, 'SCOTT', 'ANALYST', 7655, '1987-03-21', 3000, NULL, 20),

(7839, 'KING', 'PRESIDENT', NULL, '1981-11-12', 5000, NULL, 10),

(7844, 'TURNER', 'SALESMAN', 7698, '1981-09-18', 1500, NULL, 30),

(7876, 'ADAMS', 'CLERK', 7788, '1987-04-24', 1100, NULL, 20),

(7900, 'JAMES', 'CLERK', 7698, '1981-12-03', 950, NULL, 30),

(7902, 'FORD', 'ANALYST', 7655, '1981-12-03', 3000, NULL, 20), 

(7934, 'MILLER', 'CLERK', 7782, '1981-01-03', 1300, NULL, 10);

go

-- 4.1 List all the columns (with *) from the department table.

SELECT *

FROM dept;

-- 4.2 List number and name data from the department table.

SELECT deptno, dname

FROM dept;

-- 4.3 List all the columns from the employee table.

SELECT *

FROM emp;

-- 4.4 List all job data for all employees without eliminating duplicates.

SELECT job

FROM emp;

-- 4.5 List all job data for all employees and eliminate duplicates.

SELECT DISTINCT job

FROM emp;

-- 4.6 List only the employees in department 30.

SELECT *

FROM emp

WHERE deptno = 30;

-- 4.7 List the names, numbers, and departments of all clerks.

SELECT ename, empno, deptno

FROM emp

WHERE job LIKE 'CLERK';

-- 4.8 Find the names and department numbers of all departments with a department number greater than 20.

SELECT dname, deptno

FROM dept

WHERE deptno > 20;

-- 4.9 Find the names and department numbers of all departments with a department number greater than or equal to 20.

SELECT dname, deptno

FROM dept

WHERE deptno >= 20;

-- 4.10 Find the employees whose commission is greater than his salary.

SELECT *

FROM emp

WHERE comm > sal;

-- 4.11 List the name, job and salary of all employees in department 20 that has a salary of more than $2000.

SELECT ename, job, sal

FROM emp

WHERE deptno = 20 AND sal > 2000;

-- 4.12 Find all the salesmen in department 30 who have a salary greater than or equal to $1500.

SELECT *

FROM emp

WHERE deptno = 30 AND job LIKE 'SALESMAN' AND sal >= 1500;

-- 4.13 Find all the employees whose job is either manager or president.

SELECT *

FROM emp

WHERE job IN ('MANAGER', 'PRESIDENT');

-- 4.14 Find all managers who are NOT in department 30.

SELECT *

FROM emp

WHERE job LIKE 'MANAGER' AND deptno <> 30;

-- 4.15 Find all the managers in all departments, and all the clerks in department 10.

SELECT *

FROM emp

WHERE (job LIKE 'MANAGER' AND deptno <> 30) OR (job LIKE 'CLERK' AND deptno = 10);

-- 4.16 Find everyone who is neither a manager nor a clerk, but is in department 10.

SELECT *

FROM emp

WHERE job NOT IN ('MANAGER', 'CLERK') AND deptno = 10;

-- 5.1 

UPDATE emp

SET sal = sal * 1.1

WHERE job = 'SALESMAN';

-- 5.2

DELETE FROM emp

WHERE job = 'SALESMAN'
-- 1.1 Select rows within a certain range. (Using BETWEEN…AND…)

-- a. Find all the employees who earn between $1200 and $1400.

SELECT *

FROM emp

WHERE SAL BETWEEN 1200 AND 1400;

-- b. Find all the employees who do not earn between $1200 and $1400.

SELECT *

FROM emp

WHERE SAL NOT BETWEEN 1200 AND 1400;

-- 1.2 Select rows that match a value in a list. (Using IN(…) operator)

-- a. Find the employees who are clerks, analysts or salesmen.

SELECT *

FROM emp

WHERE JOB IN ('CLERK', 'ANALYST', 'SALESMAN');

-- b. Find the employees who are not clerks, analysts or salesmen.

SELECT *

FROM emp

WHERE JOB NOT IN ('CLERK', 'ANALYST', 'SALESMAN');

-- 1.3 Select rows that match a character string pattern. (Using LIKE operator)

-- a. Find all the employees whose names begin with the letter “M”.

SELECT *

FROM emp

WHERE ENAME LIKE 'M%';

-- b. Find all the employees whose names contain the letter “N”.

SELECT *

FROM emp

WHERE ENAME LIKE '%N%';

-- c. Find all the employees whose names are not 5 characters long.

SELECT *

FROM emp

WHERE LEN(ENAME) <> 5;

-- 2.1 List the employees in department 30 ordered by their salaries in ascending order.

SELECT *

FROM emp

WHERE DEPTNO = 30

ORDER BY SAL ASC;

-- 2.2 List the employees in department 30 ordered by their salaries in descending order.

SELECT *

FROM emp

WHERE DEPTNO = 30

ORDER BY SAL DESC;

-- 2.3 Order all employees by job. For those with the same job, put them in descending salary order.

SELECT *

FROM emp

ORDER BY JOB ASC, SAL DESC;

-- 3.1 The ISNULL() function.

-- Example: Calculate the average price of all books. Consider the books without price data as $20.

SELECT AVG(ISNULL(Price, 20)) FROM Books;

-- 3.2 List the name, salary, commission, and sum of salary plus commission of all salesmen.

SELECT ENAME AS name, SAL AS salary, COMM AS commission, (SAL + ISNULL(COMM, 0)) AS total_earnings

FROM emp

WHERE JOB = 'SALESMAN';

-- 3.3 List the name, salary, and commission of employees whose commissions are less than 25% of their salaries.

SELECT ENAME AS name, SAL AS salary, COMM AS commission

FROM emp

WHERE COMM < 0.25 * SAL;

-- 3.4 Calculate the total annual earnings of all salesmen based on their monthly salaries and monthly commissions.

SELECT ENAME AS name, (SAL * 12) + ISNULL(COMM * 12, 0) AS total_earnings

FROM emp

WHERE JOB = 'SALESMAN';

-- 4.1 Find the average salary for clerks.

SELECT AVG(SAL) AS average_salary

FROM emp

WHERE JOB = 'CLERK';

-- 4.2 Find the total salary and total commission for salesmen.

SELECT SUM(SAL) AS total_salary, SUM(COMM) AS total_commission

FROM emp

WHERE JOB = 'SALESMAN';

-- 4.3 Compute the average annual salary plus commission for all salesmen.

SELECT AVG((SAL * 12) + ISNULL(COMM * 12, 0)) AS average_annual_earnings

FROM emp

WHERE JOB = 'SALESMAN';

-- 4.4 Find the highest and lowest paid employee salaries and the difference between them.

SELECT MAX(SAL) AS highest_salary, MIN(SAL) AS lowest_salary, MAX(SAL) - MIN(SAL) AS salary_difference

FROM emp;

-- 4.5 Count the number of employees who receive a commission.

SELECT COUNT(*) AS commission_receiving_employees

FROM emp

WHERE COMM IS NOT NULL;

-- 4.6 Count the number of different jobs held by employees in department 30.

SELECT COUNT(DISTINCT JOB) AS unique_jobs

FROM emp

WHERE DEPTNO = 30;

-- 4.7 Count the number of employees in department 30.

SELECT COUNT(*) AS employee_count

FROM emp

WHERE DEPTNO = 30;

-- 5.1 List the department number and average salary of each department.

SELECT DEPTNO, AVG(SAL) AS average_salary

FROM emp

GROUP BY DEPTNO;

-- 5.2 Find each department’s average annual salary for all its employees except the managers and the president.

SELECT DEPTNO, AVG((SAL * 12) + ISNULL(COMM * 12, 0)) AS average_annual_salary

FROM emp

WHERE JOB NOT IN ('MANAGER', 'PRESIDENT')

GROUP BY DEPTNO;

-- 5.3 Divide all employees into groups by department, and by jobs within the department. Count the employees in each group and compute each group’s average annual salary.

SELECT DEPTNO, JOB, COUNT(*) AS employee_count, AVG((SAL * 12) + ISNULL(COMM * 12, 0)) AS average_annual_salary

FROM emp

GROUP BY DEPTNO, JOB;

-- 5.4 List the average annual salary for all job groups having more than 2 employees in the group.

SELECT JOB, AVG((SAL * 12) + ISNULL(COMM * 12, 0)) AS average_annual_salary

FROM emp

GROUP BY JOB

HAVING COUNT(*) > 2;

-- 5.5 List all the departments that have at least two clerks.

SELECT DEPTNO

FROM emp

WHERE JOB = 'CLERK'

GROUP BY DEPTNO

HAVING COUNT(*) >= 2;

-- 5.6 Find all departments with an average commission greater than 25% of the average salary.

SELECT DEPTNO

FROM emp

GROUP BY DEPTNO

HAVING AVG(COMM) > 0.25 * AVG(SAL);

-- 1.1 Create a view that contains all senior employees including managers and presidents.

CREATE VIEW SeniorEmployees AS

SELECT *

FROM EMP

WHERE JOB IN ('MANAGER', 'PRESIDENT');

-- 1.2.1 List all the senior employees who are in department 10.

SELECT *

FROM SeniorEmployees

WHERE DEPTNO = 10;

-- 1.2.2 Insert a new salesman into department 20.

INSERT INTO EMP (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO)

VALUES (9999, 'John', 'SALESMAN', 7782, SYSDATE, 2500, NULL, 20);

-- 1.2.3 List all senior employees.

SELECT *

FROM SeniorEmployees;

-- 1.3 Create a view of all employees and hide their salary and commission information in it.

CREATE VIEW EmployeesWithoutSalaryComm AS

SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, DEPTNO

FROM EMP;

-- 2.1 Define a function that, given a department number, returns the average salary of that department.

CREATE FUNCTION GetAverageSalary (@deptNo INT)

RETURNS DECIMAL(10, 2)

AS

BEGIN

    DECLARE @avgSalary DECIMAL(10, 2);

    SELECT @avgSalary = AVG(SAL)

    FROM EMP

    WHERE DEPTNO = @deptNo;

    RETURN @avgSalary;

END;

-- 2.2 Use the function in 2.1 to find employees whose salary is greater than the average salary of the department.

SELECT *

FROM EMP

WHERE SAL > dbo.GetAverageSalary(10);


-- 2.3 Create a stored procedure, given a department number, pass the number of employees and the total salary of all employees in it out to the calling statement using output parameters.

CREATE PROCEDURE GetDepartmentSummary

    @deptNo INT,

    @numEmployees INT OUTPUT,

    @totalSalary DECIMAL(10, 2) OUTPUT

AS

BEGIN

    SELECT @numEmployees = COUNT(*), @totalSalary = SUM(SAL)

    FROM EMP

    WHERE DEPTNO = @deptNo;

END;

-- 2.4 Execute the procedure in 2.3 and calculate the average salary of the department using values accessed from the output parameters.

DECLARE @numEmployees INT, @totalSalary DECIMAL(10, 2);

EXEC GetDepartmentSummary 10, @numEmployees OUTPUT, @totalSalary OUTPUT;



DECLARE @avgSalary DECIMAL(10, 2);

SET @avgSalary = @totalSalary / @numEmployees;

SELECT @avgSalary AS AverageSalary;

-- 2.5 Create a trigger that prevents the insertion of new employees whose salary is higher than 3000, and list the information of the inserted employees and rejected employees in the message window.

CREATE TRIGGER SalaryCheckTrigger ON EMP

INSTEAD OF INSERT

AS

BEGIN

    DECLARE @empNo INT, @empName VARCHAR(50), @status VARCHAR(10);

    DECLARE empCursor CURSOR FOR

        SELECT EMPNO, ENAME

        FROM inserted;
  
    OPEN empCursor;

    FETCH NEXT FROM empCursor INTO @empNo, @empName;

    WHILE @@FETCH_STATUS = 0

    BEGIN

        IF EXISTS (SELECT 1 FROM inserted WHERE EMPNO = @empNo AND SAL > 3000)

            SET @status = 'REJECTED';

        ELSE

            SET @status = 'INSERTED';



        PRINT CONVERT(VARCHAR(10), @empNo) + '  ' + @empName + '  ' + @status;     

        FETCH NEXT FROM empCursor INTO @empNo, @empName;

    END;

    

    CLOSE empCursor;

    DEALLOCATE empCursor;

END;


-- 2.6 Run the provided script to check that the trigger created in 2.5 works correctly.

DELETE FROM EMP WHERE EMPNO > 8000;

INSERT INTO EMP (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO)

VALUES

    (8369, 'ERIC', 'CLERK', 7902, '2001-12-17', 800, NULL, 20),

    (8902, 'LANCE', 'ANALYST', 7655, '2001-12-17', 3100, NULL, 20),

    (9655, 'ANDREW', 'MANAGER', 7839, '2001-12-17', 2975, NULL, 20),

    (8698, 'FRED', 'MANAGER', 7839, '2001-12-17', 2850, NULL, 30),

    (9499, 'LEE', 'SALESMAN', 7698, '2001-12-17', 1600, 300, 30),

    (8521, 'ALICE', 'SALESMAN', 7698, '2001-12-17', 3250, 500, 30),

    (8654, 'ELSA', 'SALESMAN', 7698, '2001-12-17', 1250, 1400, 30),

    (9782, 'EMILY', 'MANAGER', 7839, '2001-12-17', 4450, NULL, 10);

-- 3.1 Write a script, if the average salary of all employees is higher than 5000, print a message. If the average salary is lower than 3000, print another message.

DECLARE @avgSalary DECIMAL(10, 2);

SELECT @avgSalary = AVG(SAL) FROM EMP;

IF @avgSalary > 5000

    PRINT 'The average salary is higher than 5000.';

ELSE IF @avgSalary < 3000

    PRINT 'The average salary is lower than 3000.';

-- 3.2 Raise the salaries of all managers repeatedly by 1.1 times, until their average salary is greater than 8000. If the average salary of all employees is greater than 5000, stop the raising and print a message.

DECLARE @avgManagerSalary DECIMAL(10, 2);

WHILE (SELECT AVG(SAL) FROM EMP WHERE JOB = 'MANAGER') <= 8000

BEGIN

    UPDATE EMP SET SAL = SAL * 1.1 WHERE JOB = 'MANAGER';

END;

SELECT @avgManagerSalary = AVG(SAL) FROM EMP WHERE JOB = 'MANAGER';

IF @avgManagerSalary > 8000

    PRINT 'The average salary of managers is now greater than 8000.';

ELSE IF (SELECT AVG(SAL) FROM EMP) > 5000

    PRINT 'The average salary of all employees is already greater than 5000, stopping the raising.';