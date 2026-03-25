/* view - 1  Monthly Sales */

CREATE VIEW monthly_sales AS
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY month;

/* view - 2   Category performance */

CREATE VIEW category_performance AS
SELECT 
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales_data
GROUP BY category;

/* view - 3   Regional performance */

CREATE VIEW region_performance AS
SELECT 
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales_data
GROUP BY region;

/* view - 4   Top Customers  */

CREATE VIEW top_customers AS
SELECT 
    customer_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales_data
GROUP BY customer_name;

/* view - 5 Discount impact */

CREATE VIEW discount_analysis AS
SELECT 
    discount,
    AVG(profit) AS avg_profit
FROM sales_data
GROUP BY discount;