# Write your MySQL query statement below
WITH cte AS(SELECT user_id, visit_date, COALESCE(lead(visit_date) OVER(PARTITION BY user_id ORDER BY visit_date), DATE('2021-1-1')) as next_date 
FROM USERVisits)

SELECT user_id, MAX(DATEDIFF(next_date, visit_date)) AS biggest_window 
FROM cte
GROUP BY user_id
ORDER BY user_id ASC;