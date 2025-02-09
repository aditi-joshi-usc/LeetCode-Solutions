# Write your MySQL query statement below
SELECT Products.product_name, SUM(Orders.unit) as unit
FROM Orders INNER JOIN Products
ON Orders.product_id = Products.product_id
WHERE EXTRACT(MONTH FROM Orders.order_date) = 2 
AND  EXTRACT(YEAR FROM Orders.order_date) = 2020
GROUP BY Products.product_name 
HAVING SUM(Orders.unit)>=100;