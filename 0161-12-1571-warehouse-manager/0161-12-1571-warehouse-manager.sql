# Write your MySQL query statement below
WITH cte AS(
    SELECT product_id, width*length*height as volume
    FROM Products

)

SELECT 
    name as warehouse_name, 
    SUM(units*volume) as volume
FROM warehouse 
JOIN cte on Warehouse.product_id = cte.product_id
Group by name
;