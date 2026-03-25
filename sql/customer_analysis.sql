SELECT 
    customer_name,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 10;

/*Top 10 products */

SELECT 
    product_name,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;

/*Top categories */

SELECT 
    category,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY category
ORDER BY total_sales DESC;


/*sales based customer rankings */

SELECT 
    customer_name,
    SUM(sales) AS total_sales,
    RANK() OVER (ORDER BY SUM(sales) DESC) AS sales_rank
FROM sales_data
GROUP BY customer_name;

/*profit based customer rankings */

SELECT 
    customer_name,
    SUM(profit) AS total_profit,
    RANK() OVER (ORDER BY SUM(profit) DESC) AS profit_rank
FROM sales_data
GROUP BY customer_name;

/*combined customer rankings*/

WITH customer_stats AS (
    SELECT 
        customer_name,
        SUM(sales) AS total_sales,
        SUM(profit) AS total_profit
    FROM sales_data
    GROUP BY customer_name
)
SELECT *,
       RANK() OVER (ORDER BY total_sales DESC) AS sales_rank,
       RANK() OVER (ORDER BY total_profit DESC) AS profit_rank
FROM customer_stats;
