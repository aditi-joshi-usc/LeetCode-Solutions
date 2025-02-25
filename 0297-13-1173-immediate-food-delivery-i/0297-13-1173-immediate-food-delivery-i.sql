# Write your MySQL query statement below
WITH cte AS(
    SELECT delivery_id, 
    (
        CASE 
        WHEN order_date = customer_pref_delivery_date THEN 'immediate'
        ELSE 'scheduled'
        END
    ) AS dtype
    FROM Delivery
)

SELECT ROUND(
    SUM(
        CASE WHEN dtype = 'immediate' THEN 1
        ELSE 0
        END
    )*100/ COUNT(delivery_id)
    ,2) AS immediate_percentage 
FROM cte