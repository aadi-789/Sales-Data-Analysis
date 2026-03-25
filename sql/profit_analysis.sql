/*Profit by category*/

SELECT 
    category,
    SUM(profit) AS total_profit
FROM sales_data
GROUP BY category
ORDER BY total_profit DESC;

/*Loss making products*/

SELECT 
    product_name,
    SUM(profit) AS total_profit
FROM sales_data
GROUP BY product_name
HAVING SUM(profit) < 0
ORDER BY total_profit;


/*Profit Margin Analysis*/

SELECT 
    category,
    ROUND(SUM(profit)/SUM(sales) * 100, 2) AS profit_margin
FROM sales_data
GROUP BY category;