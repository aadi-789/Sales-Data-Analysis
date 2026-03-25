SELECT 
    DATE_TRUNC('month', order_date) AS month,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY month
ORDER BY month;


/*yearly sales trend */

SELECT 
    EXTRACT(YEAR FROM order_date) AS year,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY year
ORDER BY year;

/* month over month  growth */

SELECT 
    DATE_TRUNC('month', order_date) AS month,
    SUM(sales) AS sales,
    LAG(SUM(sales)) OVER (ORDER BY DATE_TRUNC('month', order_date)) AS prev_month_sales,
    ROUND(
        (SUM(sales) - LAG(SUM(sales)) OVER (ORDER BY DATE_TRUNC('month', order_date)))
        / LAG(SUM(sales)) OVER (ORDER BY DATE_TRUNC('month', order_date)) * 100,
        2
    ) AS growth_percentage
FROM sales_data
GROUP BY month;