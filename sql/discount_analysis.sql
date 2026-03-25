/*Discount vs Profit*/
SELECT 
    discount,
    AVG(profit) AS avg_profit
FROM sales_data
GROUP BY discount
ORDER BY discount;

/*High Discount Loss Analysis*/

SELECT *
FROM sales_data
WHERE discount > 0.3 AND profit < 0;



