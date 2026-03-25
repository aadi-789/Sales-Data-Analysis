WITH CustomerDeliveryStats AS (
    SELECT 
        customer_id,
        -- PostgreSQL simple subtraction returns an integer (number of days)
        ship_date - order_date AS delivery_time,
        quantity
    FROM sales_data
    WHERE ship_date IS NOT NULL AND order_date IS NOT NULL),

AggregatedStats AS (
    SELECT 
        customer_id,
        SUM(quantity) AS total_spent,
        -- Calculating average delivery time per customer
        ROUND(AVG(ship_date - order_date), 2) AS avg_delivery_days
    FROM sales_data
    GROUP BY customer_id
)
SELECT 
    customer_id,
    total_spent,
    avg_delivery_days,
    NTILE(4) OVER (ORDER BY total_spent DESC) AS spend_quartile,
    CASE 
        WHEN NTILE(4) OVER (ORDER BY total_spent DESC) = 1 THEN 'VIP'
        WHEN NTILE(4) OVER (ORDER BY total_spent DESC) = 2 THEN 'High Value'
        WHEN NTILE(4) OVER (ORDER BY total_spent DESC) = 3 THEN 'Standard'
        ELSE 'Low Value'
    END AS segment_label
FROM AggregatedStats
ORDER BY total_spent DESC;