-- Top 10 Countries by Revenue
SELECT Country,
       SUM(total_amount) AS total_revenue
FROM retail_sales
GROUP BY Country
ORDER BY total_revenue DESC
LIMIT 10;

-- Top 10 Customers by Revenue
SELECT CustomerID,
       SUM(total_amount) AS customer_revenue
FROM retail_sales
GROUP BY CustomerID
ORDER BY customer_revenue DESC
LIMIT 10;

-- Top 10 Products by Quantity Sold
SELECT Description,
       SUM(Quantity) AS total_quantity_sold
FROM retail_sales
GROUP BY Description
ORDER BY total_quantity_sold DESC
LIMIT 10;

-- Average Order Value
SELECT AVG(total_amount) AS average_order_value
FROM retail_sales;

-- Total Transactions by Country
SELECT Country,
       COUNT(*) AS transaction_count
FROM retail_sales
GROUP BY Country
ORDER BY transaction_count DESC;

-- Monthly Revenue Trend
SELECT SUBSTR(InvoiceDate, 4, 7) AS month,
       SUM(total_amount) AS monthly_revenue
FROM retail_sales
GROUP BY month
ORDER BY monthly_revenue DESC;

-- Highest Priced Products
SELECT Description,
       MAX(UnitPrice) AS highest_price
FROM retail_sales
GROUP BY Description
ORDER BY highest_price DESC
LIMIT 10;

-- Customers with More Than 100 Purchases
SELECT CustomerID,
       COUNT(*) AS purchase_count
FROM retail_sales
GROUP BY CustomerID
HAVING purchase_count > 100
ORDER BY purchase_count DESC;

-- Revenue Contribution by Country
SELECT Country,
       ROUND(SUM(total_amount) * 100.0 /
       (SELECT SUM(total_amount) FROM retail_sales), 2)
       AS revenue_percentage
FROM retail_sales
GROUP BY Country
ORDER BY revenue_percentage DESC;

-- Top Products by Revenue
SELECT Description,
       SUM(total_amount) AS product_revenue
FROM retail_sales
GROUP BY Description
ORDER BY product_revenue DESC
LIMIT 10;