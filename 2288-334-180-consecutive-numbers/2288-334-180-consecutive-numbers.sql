# Write your MySQL query statement below
-- SELECT DISTINCT log1.num as ConsecutiveNums
-- FROM
-- Logs log1 JOIN Logs log2
-- ON log1.num = log2.num AND log1.id = log2.id - 1
-- JOIN Logs log3
-- ON log1.num = log3.num AND log1.id = log3.id - 2;

WITH cte AS (
    SELECT num, 
    LEAD(num,1) OVER() AS num1,
    LEAD(num,2) OVER() AS num2
    FROM Logs
)

SELECT DISTINCT num AS ConsecutiveNums 
FROM cte
WHERE
num = num1 AND num = num2;