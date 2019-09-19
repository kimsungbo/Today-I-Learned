# SQL BASIC (SELECT, FROM, WEHRE)

## SELECT
used to retrieve data from tables

ex) retrieve everything

    SELECT * 
    FROM employees;

ex) retrieve a specific field

    SELECT emp_name
    FROM employees;

ex) alias

    SELECT e.emp_name
    FROM employees AS e;

ex) count the selected number of rows
    
    SELECT COUNT(e.emp_name)
    FROM employees As e;

ex) distinct values (to remove duplicates)

    SELECT DISTINCT city
    FROM station;

## function related to math

function | syntax
---------|--------
sum|SUM()
average| AVG()
maximum|MAX()
minimum|MIN()
round|ROUND()
round to nearest tenth decimal point|ROUND( x, 1)

## WHERE
Used to set conditions

ex) set conditions with inequality sign
    
    SELECT * 
    FROM employees 
    WHERE salary >= 7000;
    
### AND & OR

multiple conditions

ex) retrieve data that satisfies both of the conditions

    SELECT * 
    FROM employees as e 
    WHERE e.salary >= 5000 AND e.hire_date >= '2005-05-01';

ex) retrieve data that satisfies either one of the conditions

    SELECT * 
    FROM employees as e WHERE 
    e.salary >= 5000 or e.hire_date >= '2005-05-01';

### IN

ex) retrieve data if the value of the field is either one of the given values

    SELECT * 
    FROM employees
    WHERE salary IN (5000, 6000)
    
### BETWEEN

ex) retrieve columns that have value between the given range

    SELECT * 
    FROM employees 
    WHERE salary BETWEEN 5000 AND 7000;

### LIKE

ex) retrieve columns that has city name ending with 'a'
    SELECT * 
    FROM station 
    WHERE city LIKE '%a';

### NOT LIKE

ex) retrieve columns from table which of its city name does not start with a

    SELECT * 
    FROM station 
    WHERE city NOT LIKE 'a%';

### REGEXP

used to retrieve data that matches the given regular expression

ex) retrieve distinct city names that starts with vowels

    SELECT DISTINCT city 
    FROM station 
    WHERE city REGEXP '^a|^e|^i|^o|^u';


### MOD
calculate remainder

ex) retrieve columns that have even value for their id number

    SELECT * 
    FROM station 
    WHERE MOD(id, 2) = 0;
    
### COUNT
count number of columns

ex) count number of cities

    SELECT count(city)
    FROM station;

ex) count number of distinct cities

    SELECT count(DISTINCT city) 
    FROM station;




