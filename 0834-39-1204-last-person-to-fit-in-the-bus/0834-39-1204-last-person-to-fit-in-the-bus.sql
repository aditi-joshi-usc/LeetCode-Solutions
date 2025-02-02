# Write your MySQL query statement below
WITH cte AS(
    SELECT person_id, person_name, weight, turn, 
    SUM(weight) OVER(ORDER BY turn) as tot_weight
    FROM Queue
)
select person_name 
from cte
where tot_weight<=1000
order by tot_weight DESC LIMIT 1