/* 
https://mode.com/sql-tutorial/sql-avg
Write a query that calculates the average daily trade volume for Apple stock.
*/
SELECT count(*) - count(volume)
FROM tutorial.aapl_historical_stock_price;

/*
https://mode.com/sql-tutorial/sql-group-by
Calculate the total number of shares traded each month. Order your results chronologically.
*/
SELECT year
      , month
      , SUM(volume)
FROM tutorial.aapl_historical_stock_price
GROUP BY year, month
ORDER BY year, month;

-- Write a query to calculate the average daily price change in Apple stock, grouped by year.
SELECT year
      , AVG(high - low)
FROM tutorial.aapl_historical_stock_price
GROUP BY year;

SELECT * FROM tutorial.aapl_historical_stock_price;

-- Write a query that calculates the lowest and highest prices that Apple stock achieved each month.
SELECT year
      , month
      , MIN(low)
      , MAX(high)
FROM tutorial.aapl_historical_stock_price
GROUP BY year, month
ORDER BY year, month;

-- https://mode.com/sql-tutorial/sql-having
SELECT year
      , month
      , MAX(high) AS month_high
FROM tutorial.aapl_historical_stock_price
GROUP BY year, month
HAVING MAX(high) > 400
ORDER BY year, month;

-- https://mode.com/sql-tutorial/sql-distinct
SELECT COUNT(DISTINCT year)
FROM tutorial.aapl_historical_stock_price;

-- Write a query that returns the unique values in the year column, in chronological order.
SELECT DISTINCT year
FROM tutorial.aapl_historical_stock_price
ORDER BY year;

-- Write a query that separately counts the number of unique values in the month column and the number of unique values in the `year` column.
SELECT COUNT(DISTINCT year) count_year
      , COUNT(DISTINCT month) count_month
FROM tutorial.aapl_historical_stock_price;