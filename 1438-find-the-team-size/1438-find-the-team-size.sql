# Write your MySQL query statement below
WITH teamCount AS(
    SELECT team_id, COUNT(employee_id) as cnt
    FROM Employee 
    GROUP BY team_id
)

SELECT e.employee_id, t.cnt AS team_size  
FROM Employee AS e LEFT JOIN teamCount AS t
ON e.team_id = t.team_id;