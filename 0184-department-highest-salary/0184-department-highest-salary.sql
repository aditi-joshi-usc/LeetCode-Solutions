# Write your MySQL query statement below
WITH cte AS (SELECT d.name AS Department , e.name AS Employee, 
salary, RANK() OVER(PARTITION BY e.departmentId ORDER BY salary DESC) AS rank_sal
FROM Employee AS e 
INNER JOIN Department AS d
ON e.departmentId = d.id)

SELECT Department, Employee, salary 
FROM cte
WHERE rank_sal =1;