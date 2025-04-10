-- Create Database
CREATE DATABASE OnlineBookstore;


-- Switch to the database
use OnlineBookstore;


-- Create Tables
DROP TABLE IF EXISTS Books;
CREATE TABLE Books (
    Book_ID SERIAL PRIMARY KEY,
    Title VARCHAR(100),
    Author VARCHAR(100),
    Genre VARCHAR(50),
    Published_Year INT,
    Price NUMERIC(10, 2),
    Stock INT
);



DROP TABLE IF EXISTS customers;
CREATE TABLE Customers (
    Customer_ID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(15),
    City VARCHAR(50),
    Country VARCHAR(150)
);

DROP TABLE IF EXISTS orders;
CREATE TABLE Orders (
    Order_ID SERIAL PRIMARY KEY,
    Customer_ID INT REFERENCES Customers(Customer_ID),
    Book_ID INT REFERENCES Books(Book_ID),
    Order_Date DATE,
    Quantity INT,
    Total_Amount NUMERIC(10, 2)
);

SELECT * FROM Books;

SELECT * FROM Customers;
SELECT * FROM Orders;


-- 1) Retrieve all books in the "Fiction" genre:
select * from books
where Genre='Fiction';

-- 2) Find books published after the year 1950:
select * from books
where published_year>1950;

-- 3) List all customers from the Canada:
select*from customers
where Country="Canada";

-- 4) Show orders placed in November 2023:
SELECT *
FROM orders
WHERE order_date between ('2023-11-01') AND "2023-11-30";


-- 5) Retrieve the total stock of books available:
select sum(Stock) from books;

-- 6) Find the details of the most expensive book:
select *  from books
order by price desc
limit 1;

-- 7) Show all customers who ordered more than 1 quantity of a book:
select*from orders
where Quantity>1;

-- 8) Retrieve all orders where the total amount exceeds $20:
select * from orders
where Total_Amount>20;

-- 9) List all genres available in the Books table:
select distinct Genre from books;

-- 10) Find the book with the lowest stock:
select *from books
order by Stock asc
limit 1;

-- 11) Calculate the total revenue generated from all orders:
select sum(Total_Amount)  from orders;

-- Advance Questions : 

-- 1) Retrieve the total number of books sold for each genre:
SELECT b.Genre, SUM(o.Quantity) AS Total_Books_Sold
FROM orders o
JOIN Books b ON o.Book_ID =' b.Books_ID'
GROUP BY b.Genre;

-- 2) Find the average price of books in the "Fantasy" genre:
SELECT AVG(Price) AS Average_Fantasy_Book_Price
FROM Books
WHERE Genre = 'Fantasy';

-- 3) List customers who have placed at least 2 orders:
SELECT Customer_ID, COUNT(*) FROM orders
GROUP BY Customer_ID
HAVING COUNT(*) >= 2;

-- 4) Find the most frequently ordered book:
SELECT b.Title, SUM(o.Quantity) AS orders_count
FROM orders o
JOIN Books b ON o.Book_ID = b.Book_ID
GROUP BY b.Title
ORDER BY orders_count DESC
LIMIT 1;

-- 5) Show the top 3 most expensive books of 'Fantasy' Genre :
SELECT Title, Genre, Price
FROM Books
WHERE Genre = 'Fantasy'
ORDER BY Price DESC
LIMIT 3;

-- 6) Retrieve the total quantity of books sold by each author:
SELECT b.Author, SUM(o.Quantity)
FROM orders o
JOIN Books b ON o.Book_ID = b.Book_ID
GROUP BY b.Author;

-- 7) List the cities where customers who spent over $30 are located:
SELECT DISTINCT c.City, o.Total_Amount  
FROM Orders o  
JOIN Customers c ON o.Customer_ID = c.Customer_ID  
WHERE o.Total_Amount > 10;  

-- 8) Find the customer who spent the most on orders:
SELECT c.Customer_ID,
c.Name AS Customer_Name, 
SUM(o.Quantity * b.Price) AS Total_Spent
FROM Customers c 
JOIN Orders o ON c.Customer_ID = o.Customer_ID
JOIN Books b ON o.Book_ID = b.Book_ID
GROUP BY c.Customer_ID, c.Name
ORDER BY Total_Spent DESC
LIMIT 1;

-- 9) Calculate the stock remaining after fulfilling all orders:
SELECT b.Book_ID,b.Title,b.Stock,
IFNULL(SUM(o.Quantity), 0) AS Total_Sold,
b.Stock - IFNULL(SUM(o.Quantity), 0) AS Stock_Remaining
FROM Books b
LEFT JOIN Orders o ON b.Book_ID = o.Book_ID
GROUP BY b.Book_ID, b.Title, b.Stock;

-- Here’s a concise **Conclusion** you can add to the end of your SQL project report or documentation:
-- ## ✅ **Conclusion**
-- The **Online Bookstore SQL Project** effectively demonstrates the practical application of SQL in managing and analyzing a relational
-- database system for an e-commerce setting. Through the creation of structured tables (`Books`, `Customers`, and `Orders`) and
-- implementation of a wide range of SQL queries, this project covers:
--  **Database design** with proper use of keys and constraints  
-- **Data retrieval** and filtering using `WHERE`, `LIKE`, `BETWEEN`  
--  **Joins and aggregations** for generating business insights  
--  **Real-world analysis** like top-selling books, revenue calculation, and customer behavior
-- Advanced queries showcase how SQL can be used not just for storing and retrieving data, 
-- but also for making informed decisions like tracking inventory, identifying high-value customers, and understanding genre-based sales trends.

-- This project lays a strong foundation for more complex applications such as reporting dashboards,
-- recommendation systems, or integrating the backend of a data analyze bookstore web app.





