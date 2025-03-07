# Write your MySQL query statement below
SELECT a.employee_id
FROM 
Employees AS a
LEFT JOIN Employees AS b
ON a.manager_id = b.employee_id
LEFT JOIN Employees AS c
ON b.manager_id = c.employee_id
WHERE a.employee_id != 1
AND c.manager_id = 1;