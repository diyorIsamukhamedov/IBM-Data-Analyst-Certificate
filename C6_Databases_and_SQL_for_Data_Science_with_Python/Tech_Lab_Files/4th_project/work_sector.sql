DROP TABLE IF EXISTS EMPLOYEES;
DROP TABLE IF EXISTS JOB_HISTORY;
DROP TABLE IF EXISTS JOBS;
DROP TABLE IF EXISTS DEPARTMENTS;
DROP TABLE IF EXISTS LOCATIONS;

-- =========================
-- SECTION 1: Schema
-- =========================
CREATE TABLE EMPLOYEES (
                            EMP_ID CHAR(9) NOT NULL, 
                            F_NAME VARCHAR(15) NOT NULL,
                            L_NAME VARCHAR(15) NOT NULL,
                            SSN CHAR(9),
                            B_DATE DATE,
                            SEX CHAR,
                            ADDRESS VARCHAR(30),
                            JOB_ID CHAR(9),
                            SALARY DECIMAL(10,2),
                            MANAGER_ID CHAR(9),
                            DEP_ID CHAR(9) NOT NULL,
                            PRIMARY KEY (EMP_ID));
                            
  CREATE TABLE JOB_HISTORY (
                            EMPL_ID CHAR(9) NOT NULL, 
                            START_DATE DATE,
                            JOBS_ID CHAR(9) NOT NULL,
                            DEPT_ID CHAR(9),
                            PRIMARY KEY (EMPL_ID,JOBS_ID));
 
 CREATE TABLE JOBS (
                            JOB_IDENT CHAR(9) NOT NULL, 
                            JOB_TITLE VARCHAR(30),
                            MIN_SALARY DECIMAL(10,2),
                            MAX_SALARY DECIMAL(10,2),
                            PRIMARY KEY (JOB_IDENT));

CREATE TABLE DEPARTMENTS (
                            DEPT_ID_DEP CHAR(9) NOT NULL, 
                            DEP_NAME VARCHAR(15) ,
                            MANAGER_ID CHAR(9),
                            LOC_ID CHAR(9),
                            PRIMARY KEY (DEPT_ID_DEP));

CREATE TABLE LOCATIONS (
                            LOCT_ID CHAR(9) NOT NULL,
                            DEP_ID_LOC CHAR(9) NOT NULL,
                            PRIMARY KEY (LOCT_ID,DEP_ID_LOC));
-- ================================================================================

-- =========================
-- SECTION 2: Insert Data via built-in Data Transfer feature of DBeaver
-- =========================
-- ================================================================================

-- =========================
-- SECTION 3: Sub-queries and Nested Selects (practice)
-- =========================
SELECT * 
FROM employees
WHERE salary < (SELECT avg(salary) FROM employees);
-- =========================
SELECT emp_id, salary, (SELECT max(salary) FROM employees) AS max_salary
FROM employees;
-- =========================
SELECT f_name, l_name
FROM employees
WHERE b_date = (SELECT min(b_date) FROM employees);
-- =========================
SELECT avg(salary)
FROM (
	SELECT salary
	FROM employees
	ORDER BY salary DESC
	LIMIT 5
	 ) AS salary_table;
-- ================================================================================

/*
  
 1. Write a query to find the average salary of the five least-earning employees. 
  
*/

SELECT avg(salary)
FROM (
	SELECT salary
	FROM employees
	ORDER BY salary
	LIMIT 5
	 ) AS salary_table;

-- ================================================================================

/*
  
 2. Write a query to find the records of employees older than the average age of all employees. 
  
*/

-- MySQL syntax
SELECT * 
FROM EMPLOYEES 
WHERE YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE,B_DATE))) > 
    (SELECT AVG(YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE,B_DATE)))) 
    FROM EMPLOYEES);
-- PostgreSQL syntax
SELECT *
FROM employees
WHERE EXTRACT(YEAR FROM age(current_date, b_date)) >
	  (SELECT avg(EXTRACT (YEAR FROM age(current_date, b_date))) FROM employees);

-- ================================================================================

/*
  
 3. From the Job_History table, display the list of Employee IDs, years of service, and average years of service for all entries. 
  
*/

-- MySQL syntax
SELECT EMPL_ID, YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, START_DATE))), 
    (SELECT AVG(YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, START_DATE)))) 
    FROM JOB_HISTORY)
FROM JOB_HISTORY;
-- PostgreSQL syntax
SELECT 
	empl_id,
	EXTRACT(YEAR FROM age(current_date, start_date)) AS years_of_service,
	(SELECT avg(EXTRACT(YEAR FROM age(current_date, start_date))) FROM job_history) AS avg_years_of_service
FROM job_history;

-- ================================================================================
































