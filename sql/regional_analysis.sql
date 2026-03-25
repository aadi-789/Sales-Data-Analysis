/*region wise sales and profit analysis*/
SELECT 
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales_data
GROUP BY region;

/*state wise performance analysis*/ 

SELECT 
    state,
    SUM(sales),
    SUM(profit)
FROM sales_data
GROUP BY state
ORDER BY SUM(sales) DESC;