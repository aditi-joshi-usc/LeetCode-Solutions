# Write your MySQL query statement below

SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM Activity
GROUP BY activity_date HAVING active_users>0 AND activity_date > "2019-06-27" AND activity_date <= "2019-07-27";