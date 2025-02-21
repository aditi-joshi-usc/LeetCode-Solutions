# Write your MySQL query statement below
-- with cte AS(
--     SELECT a.customer_id
--     FROM
--     Orders AS a
--     JOIN Orders AS B
--     ON a.customer_id = b.customer_id
--     AND a.product_name = 'A' AND b.product_name = 'B'
--     )
-- ,
-- cte2 AS(
-- SELECT 
--     customer_id from Orders 
--     WHERE product_name = 'C'
-- )

-- SELECT customer_id, customer_name
-- FROM Customers
-- WHERE customer_id IN (Select customer_id from cte)
-- AND customer_id NOT IN (Select customer_id from cte2)
-- ORDER BY customer_id;

SELECT customer_id, customer_name
FROM Customers
WHERE customer_id IN(
    SELECT customer_id
    FROM orders
    GROUP BY customer_id
    HAVING SUM(product_name = 'A') >=1 AND SUM(product_name = 'B') >=1
    AND SUM(product_name = 'C') = 0)
ORDER BY customer_id;

