# Write your MySQL query statement below
WITH cte AS(
    SELECT order_id, customer_id, product_id, COUNT(order_id) AS cnt  FROM
    Orders 
    GROUP BY customer_id, product_id
),
cte2 AS(
    SELECT customer_id, product_id,
    DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY cnt DESC) as rankid FROM cte
)
SELECT cte2.customer_id, cte2.product_id, p.product_name
FROM cte2 INNER JOIN Products AS p
ON cte2.product_id = p.product_id WHERE rankid = 1; 