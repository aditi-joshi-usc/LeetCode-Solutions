# Write your MySQL query statement below
WITH cte AS (SELECT user_id, COUNT(movie_id) as cnt
FROM MovieRating  
GROUP BY user_id 
),


cte2 AS (SELECT movie_id, AVG(rating) as rate
FROM MovieRating  
WHERE created_at >= '2020-02-01' AND created_at <= '2020-02-29' 
GROUP BY movie_id 
)

SELECT MIN(name) AS results
FROM Users 
WHERE user_id IN(
SELECT user_id from cte where cnt = (SELECT MAX(cnt) FROM cte))
UNION ALL
SELECT MIN(title) AS results
FROM Movies 
WHERE movie_id IN(
SELECT movie_id from cte2 where rate = (SELECT MAX(rate) FROM cte2));