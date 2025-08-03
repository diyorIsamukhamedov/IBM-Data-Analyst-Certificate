DROP TABLE IF EXISTS petrescue;

CREATE TABLE  petrescue (
	id integer NOT NULL,
	animal varchar(20),
	quantity integer,
	cost decimal(6, 2),
	rescuedate date,
	PRIMARY KEY (id)
);

INSERT INTO petrescue (id, animal, quantity, cost, rescuedate)
VALUES 
	(1,'Cat',9,450.09,'2018-05-29'),
	(2,'Dog',3,666.66,'2018-06-01'),
	(3,'Dog',1,100.00,'2018-06-04'),
	(4,'Parrot',2,50.00,'2018-06-04'),
	(5,'Dog',1,75.75,'2018-06-10'),
	(6,'Hamster',6,60.60,'2018-06-11'),
	(7,'Cat',1,44.44,'2018-06-11'),
	(8,'Goldfish',24,48.48,'2018-06-14'),
	(9,'Dog',2,222.22,'2018-06-15');

-- practice

-- MySQL syntax
SELECT DAY(RESCUEDATE) FROM PETRESCUE;
-- PostgreSQL syntax
SELECT EXTRACT(DAY FROM rescuedate) FROM petrescue;

-- MySQL syntax
SELECT MONTH(RESCUEDATE) FROM PETRESCUE;
-- PostgreSQL syntax
SELECT EXTRACT(MONTH FROM rescuedate) FROM petrescue;

-- MySQL syntax
SELECT YEAR(RESCUEDATE) FROM PETRESCUE;
-- PostgreSQL syntax
SELECT EXTRACT(YEAR FROM rescuedate) FROM petrescue;

-- MySQL syntax
SELECT DATE_ADD(RESCUEDATE, INTERVAL 3 DAY) FROM PETRESCUE
-- PostgreSQL syntax
SELECT rescuedate + INTERVAL '3 days' FROM petrescue;

-- MySQL syntax
SELECT DATE_ADD(RESCUEDATE, INTERVAL 2 MONTH) FROM PETRESCUE
-- PostgreSQL syntax
SELECT rescuedate + INTERVAL '2 month' FROM petrescue;

-- MySQL syntax
SELECT DATE_SUB(RESCUEDATE, INTERVAL 3 DAY) FROM PETRESCUE
-- PostgreSQL syntax
SELECT rescuedate - INTERVAL '3 days' FROM petrescue;

-- MySQL syntax
SELECT DATEDIFF(CURRENT_DATE, RESCUEDATE) FROM PETRESCUE
-- PostgreSQL syntax
SELECT current_date - rescuedate FROM petrescue;
-- ================================================================================

/*
  
 1. Write a query that displays the average cost of rescuing a single dog.
 Note that the cost per dog would not be the same in different instances.  
  
*/

SELECT avg(COST / quantity) 
FROM petrescue
WHERE animal = 'Dog';
-- ================================================================================

/*

 2. Write a query that displays the animal name in each rescue in uppercase without duplications. 
  
*/

-- MySQL syntax
SELECT DISTINCT ucase(animal) FROM petrescue;

-- PostgreSQL syntax
SELECT DISTINCT upper(animal) FROM petrescue;
-- ================================================================================

/*

 3. Write a query that displays all the columns from the PETRESCUE table where the animal(s) rescued are cats. 
 Use cat in lowercase in the query.
  
*/

-- MySQL syntax
SELECT * FROM PETRESCUE WHERE LCASE(ANIMAL) = "cat";
-- PostgreSQL syntax
SELECT * FROM petrescue WHERE lower(animal) = 'cat';
-- ================================================================================

/*
  
 4. Write a query that displays the number of rescues in the 5th month.  
  
*/

-- MySQL syntax
SELECT SUM(QUANTITY) FROM PETRESCUE WHERE MONTH(RESCUEDATE)="05";
-- PostgreSQL syntax
SELECT sum(quantity)
FROM petrescue
WHERE EXTRACT(MONTH FROM rescuedate) = 5;
-- ================================================================================

/*
  
 5. The rescue shelter is supposed to find good homes for all animals within 1 year of their rescue. 
 	Write a query that displays the ID and the target date.
  
*/

-- MySQL syntax
SELECT ID, DATE_ADD(RESCUEDATE, INTERVAL 1 YEAR) FROM PETRESCUE;
-- PostgreSQL syntax
SELECT id, rescuedate + INTERVAL '1 year' FROM petrescue;
-- ================================================================================