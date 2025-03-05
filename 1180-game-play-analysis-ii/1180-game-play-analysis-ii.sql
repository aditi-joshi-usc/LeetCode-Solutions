# Write your MySQL query statement below
-- SELECT player_id, device_id
-- FROM
-- (
--     SELECT player_id, device_id, RANK() OVER(PARTITION BY player_id ORDER BY event_date) AS date_rank FROM Activity 
-- ) AS t
-- where date_rank = 1;

SELECT DISTINCT player_id, FIRST_VALUE(device_id)
OVER(PARTITION BY player_id ORDER BY event_date) as device_id
FROM Activity;