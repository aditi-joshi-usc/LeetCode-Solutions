# Write your MySQL query statement below
SELECT * from Cinema 
WHERE id%2 <>0 and description not LIKE "%boring%" 
ORDER BY rating DESC;