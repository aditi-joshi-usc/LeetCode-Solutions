# Write your MySQL query statement below
SELECT 
    DISTINCT s1.seat_id
FROM Cinema AS s1 INNER JOIN Cinema AS s2 ON abs(s1.seat_id - s2.seat_id) = 1
WHERE s1.free = 1 AND s2.free=1
ORDER BY s1.seat_id;