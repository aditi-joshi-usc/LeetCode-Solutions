# Write your MySQL query statement below
SELECT 
    name
FROM SalesPerson 
WHERE
sales_id NOT IN(
    SELECT orders.sales_id from Orders
    join company on orders.com_id = company.com_id
    where company.name = 'RED'

);
