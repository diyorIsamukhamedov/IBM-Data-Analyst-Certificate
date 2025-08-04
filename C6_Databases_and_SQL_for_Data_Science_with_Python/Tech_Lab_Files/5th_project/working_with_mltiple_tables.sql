DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS job_history;
DROP TABLE IF EXISTS jobs;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS locations;

-- =========================
-- SECTION 1: Schema
-- =========================
CREATE TABLE employees (
	emp_id char(9) NOT NULL,
	f_name varchar(25) NOT NULL,
	l_name varchar(25) NOT NULL,
	ssn char(9),
	b_date date,
	sex char,
	address varchar(30),
	job_id char(9),
	salary decimal(10, 2),
	manager_id char(9),
	dep_id char(9) NOT NULL,
	PRIMARY KEY (emp_id)
);

CREATE TABLE job_history (
	empl_id char(9) NOT NULL,
	start_date date,
	jobs_id char(9) NOT NULL,
	dept_id char(9),
	PRIMARY KEY (empl_id, jobs_id)
);

CREATE TABLE jobs (
	job_ident char(9) NOT NULL,
	job_title varchar(30),
	min_salary decimal(10, 2),
	max_salary decimal(10, 2),
	PRIMARY KEY (job_ident)
);

CREATE TABLE departments (
	dept_id_dep char(9) NOT NULL,
	dep_name varchar(15),
	manager_id char(9),
	loc_id char(9),
	PRIMARY KEY (dept_id_dep)
);

CREATE TABLE locations (
	loct_id char(9) NOT NULL,
	dep_id_loc char(9) NOT NULL,
	PRIMARY KEY (loct_id, dep_id_loc)
);
-- ================================================================================

-- =========================
-- SECTION 2: Cheking tables (select * from table_name)
-- =========================
SELECT * FROM employees;
SELECT * FROM job_history;
SELECT * FROM jobs;
SELECT * FROM departments;
SELECT * FROM locations;
-- ================================================================================

-- =========================
-- SECTION 3: Insert Data via built-in Data Transfer feature of DBeaver
-- =========================
-- ================================================================================

-- =========================
-- SECTION 4: Working with Multiple Tables (practice)
-- =========================
-- Accessing multiple tables with sub-queries
-- 1. Retrieve only the EMPLOYEES records corresponding to jobs in the JOBS table.
SELECT * FROM employees WHERE job_id IN (SELECT job_ident FROM jobs);
-- 2. Retrieve JOB information for employees earning over $70,000.
SELECT job_title, min_salary, max_salary, job_ident
FROM jobs
WHERE job_ident IN (SELECT job_id FROM employees WHERE salary > 70000);
-- =========================
-- Accessing multiple tables with Implicit Joins
-- 1. Retrieve only the EMPLOYEES records corresponding to jobs in the JOBS table.
SELECT *
FROM employees, jobs
WHERE employees.job_id = jobs.job_ident;
-- 2. Redo the previous query using shorter aliases for table names.
SELECT *
FROM employees e, jobs j
WHERE e.job_id = j.job_ident;
-- 3. In the previous query, retrieve only the Employee ID, Name, and Job Title.
SELECT emp_id, f_name, l_name, job_title
FROM employees e, jobs j
WHERE e.job_id = j.job_ident;
-- 4. Redo the previous query, but specify the fully qualified column names with aliases in the SELECT clause.
SELECT e.emp_id, e.f_name, e.l_name, j.job_title
FROM employees e, jobs j
WHERE e.job_id = j.job_ident;
-- ================================================================================

/*
  
 1. Retrieve only the list of employees whose JOB_TITLE is Jr. Designer. 
  
*/

-- a. Using sub-queries
SELECT *
FROM employees
WHERE job_id IN (SELECT job_ident 
				 FROM jobs 
				 WHERE job_title = 'Jr. Designer');

-- b. Using Implicit Joins
SELECT *
FROM employees e, jobs j
WHERE e.job_id = j.job_ident AND j.job_title = 'Jr. Designer';

/*
  
 2. Retrieve JOB information and a list of employees whose birth year is after 1976.
  
*/

-- a. Using sub-queries
-- MySQL syntax
SELECT JOB_TITLE, MIN_SALARY, MAX_SALARY, JOB_IDENT
FROM JOBS
WHERE JOB_IDENT IN (SELECT JOB_ID
                    FROM EMPLOYEES
                    WHERE YEAR(B_DATE)>1976 );
-- PostgreSQL syntax
SELECT job_title, min_salary, max_salary, job_ident
FROM jobs
WHERE job_ident IN (
	SELECT job_id 
	FROM employees
	WHERE EXTRACT(YEAR FROM b_date) > 1976
);
-- b. Using Implicit Joins
-- MySQL syntax
SELECT J.JOB_TITLE, J.MIN_SALARY, J.MAX_SALARY, J.JOB_IDENT
FROM JOBS J, EMPLOYEES E
WHERE E.JOB_ID = J.JOB_IDENT AND YEAR(E.B_DATE)>1976;
-- PostgreSQL syntax
SELECT j.job_title, j.min_salary, j.max_salary, j.job_ident
FROM jobs j, employees e
WHERE j.job_ident = e.job_id AND EXTRACT(YEAR FROM e.b_date) > 1976;
-- ================================================================================









































