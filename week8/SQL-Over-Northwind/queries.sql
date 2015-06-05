SELECT FirstName, LastName, Title
FROM employees;

SELECT FirstName, LastName, Title, City
FROM employees
WHERE City = "Seattle";

SELECT FirstName, LastName, Title, City
FROM employees
WHERE City = "London";

SELECT FirstName, LastName, Title, City
FROM employees
WHERE  Title like '%Sales%';

SELECT FirstName, LastName, Title, City, TitleOfCourtesy
FROM employees
WHERE  Title LIKE '%Sales%' AND  TitleOfCourtesy IN ('Ms.' , 'Mrs.') ;

SELECT FirstName, LastName, Title, BirthDate
FROM employees
ORDER BY BirthDate ASC
LIMIT 5;

SELECT FirstName, LastName, Title, HireDate
FROM employees
ORDER BY HireDate ASC
LIMIT 5;

SELECT  FirstName, LastName, Title, ReportsTo
FROM employees
WHERE ReportsTo IS NULL;

SELECT  emp.EmployeeID, emp.FirstName || ' ' || emp.LastName as employee , emp.Title, emp.ReportsTo, bs.FirstName || ' ' || bs.LastName as boss
FROM employees emp, employees bs
WHERE emp.ReportsTo = bs.EmployeeID;

SELECT count(EmployeeID) 
FROM employees
WHERE TitleOfCourtesy IN ('Ms.' , 'Mrs.') ;

SELECT count(EmployeeID) 
FROM employees
WHERE TitleOfCourtesy IN ('Ms.' , 'Mrs.') ;


SELECT count(EmployeeID) 
FROM employees
WHERE TitleOfCourtesy = 'Mr.' ;

SELECT count(EmployeeID), City 
FROM employees
GROUP BY City;


SELECT o.OrderID, e.FirstName, e.LastName 
FROM employees e
JOIN orders o
ON e.EmployeeID = o. EmployeeID;


SELECT o.OrderID, s.CompanyName
FROM shippers s
JOIN orders o
ON s.ShipperID = o.ShipVia;

SELECT COUNT(OrderID), ShipCountry
FROM orders
GROUP BY  ShipCountry;


SELECT COUNT(o.OrderID) AS number_of_orders, o.EmployeeID, e.FirstName, e.LastName
FROM orders o
JOIN employees e
ON o.EmployeeID = e.EmployeeID
GROUP BY o.EmployeeID, e.FirstName, e.LastName
ORDER BY number_of_orders DESC
LIMIT 1;


SELECT count(o.OrderID) number_of_orders, c.CompanyName, c.Country
FROM customers c
JOIN orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.CompanyName, c.Country
ORDER BY number_of_orders DESC
LIMIT 1;


SELECT o.OrderID, e.FirstName||' '||e.LastName as employee_name, c.CompanyName
FROM orders o
JOIN employees e
ON o.EmployeeID = e.EmployeeID
JOIN customers c
ON o.CustomerID = c.CustomerID;

SELECT c.CustomerID, c.CompanyName as customer, s.CompanyName as shipper
FROM orders o
JOIN customers c
ON c.CustomerID = o.CustomerID
JOIN shippers s
ON o.ShipVia = s.ShipperID;