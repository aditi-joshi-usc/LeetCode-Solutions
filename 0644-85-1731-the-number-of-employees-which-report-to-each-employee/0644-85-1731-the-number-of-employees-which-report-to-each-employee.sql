# Write your MySQL query statement below
SELECT manager.employee_id, manager.name, COUNT(employ.employee_id) as reports_count, ROUND(AVG(employ.age),0) AS average_age
FROM Employees manager
JOIN Employees employ
ON manager.employee_id = employ.reports_to
GROUP BY manager.employee_id 
ORDER BY manager.employee_id ASC;