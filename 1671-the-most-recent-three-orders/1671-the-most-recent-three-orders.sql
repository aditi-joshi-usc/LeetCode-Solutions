# Write your MySQL query statement below
WITH cte AS (SELECT 
    c.name, o.customer_id, o.order_id, 
    o.order_date, DENSE_RANK() OVER(PARTITION BY o.customer_id ORDER BY o.order_date DESC) AS rankid
FROM Orders AS o
INNER JOIN Customers AS c
ON o.customer_id = c.customer_id)

SELECT name as customer_name, customer_id, order_id, order_date 
FROM cte 
WHERE rankid<=3
ORDER BY name ASC, customer_id ASC, order_date DESC ;