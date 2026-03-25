WITH rfm_base AS (
    SELECT 
        customer_name,
        MAX(order_date) AS last_order_date,
        COUNT(order_id) AS frequency,
        SUM(sales) AS monetary,
        ROUND(AVG(ship_date - order_date), 2) AS avg_delivery_days
    FROM sales_data
    GROUP BY customer_name
),

rfm_calc AS (
    SELECT 
        customer_name,
        (CURRENT_DATE - last_order_date) AS recency,
        frequency,
        monetary,
        avg_delivery_days
    FROM rfm_base
),

rfm_scores AS (
    SELECT 
        *,
        NTILE(5) OVER (ORDER BY recency DESC) AS r_score,
        NTILE(5) OVER (ORDER BY frequency ASC) AS f_score,
        NTILE(5) OVER (ORDER BY monetary ASC) AS m_score
    FROM rfm_calc
)

SELECT 
    *,
    CONCAT(r_score, f_score, m_score) AS rfm_segment,

    CASE 
        WHEN CONCAT(r_score, f_score, m_score) = '555' THEN 'Best Customers'
        WHEN r_score >= 4 AND f_score >= 4 THEN 'Loyal Customers'
        WHEN r_score <= 2 THEN 'At Risk'
        ELSE 'Average Customers'
    END AS customer_segment

FROM rfm_scores
ORDER BY monetary DESC;