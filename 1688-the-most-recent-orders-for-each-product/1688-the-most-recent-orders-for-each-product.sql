# Write your MySQL query statement below
WITH cte AS(
    select p.product_name AS product_name, 
    o.product_id AS product_id ,
    o.order_id AS order_id ,
    o.order_date as order_date,
    RANK() OVER(PARTITION BY o.product_id ORDER BY o.order_date DESC) as rankid 
    from Orders AS o LEFT JOIN Products AS p
    ON o.product_id = p.product_id
)

SELECT product_name, product_id, order_id, order_date
FROM cte 
WHERE rankid =1
ORDER BY product_name, product_id, order_id;