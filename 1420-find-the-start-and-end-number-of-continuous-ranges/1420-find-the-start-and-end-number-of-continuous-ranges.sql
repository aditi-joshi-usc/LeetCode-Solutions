# Write your MySQL query statement below
WITH cte AS(
SELECT log_id AS dt,
log_id - rank() OVER(order by log_id) as rankid
from Logs)

SELECT min(dt) AS start_id, max(dt) AS end_id
FROM cte
GROUP BY rankid;