# Write your MySQL query statement below

SELECT contest_id, ROUND(COUNT(user_id) * 100 / (select count(*) from Users),2) as percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC
;