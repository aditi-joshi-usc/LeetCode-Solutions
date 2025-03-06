# Write your MySQL query statement below
WITH cte AS(SELECT 
    p.project_id, p.employee_id,
    DENSE_RANK() OVER(PARTITION BY p.project_id ORDER BY experience_years DESC) AS rankid
FROM Project AS p
INNER JOIN Employee AS e
ON p.employee_id = e.employee_id)

SELECT project_id, employee_id
FROM cte WHERE rankid = 1;