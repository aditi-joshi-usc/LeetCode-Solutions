# Write your MySQL query statement below


-- WITH cte AS(
--     SELECT e.employee_id FROM Employees AS e LEFT JOIN Salaries AS s ON e.employee_id = s.employee_id where s.salary is null
-- UNION
-- SELECT s.employee_id FROM Employees AS e RIGHT JOIN Salaries AS s ON e.employee_id = s.employee_id where e.name is null
-- )
-- SELECT DISTINCT employee_id FROM cte 
-- order by employee_id;


SELECT employee_id from employees where employee_id NOT IN (SELECT employee_id from Salaries)
UNION
SELECT employee_id from Salaries where employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;