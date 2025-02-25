# Write your MySQL query statement below
WITH Calls2 AS(
    SELECT 
    (CASE WHEN from_id > to_id THEN to_id ELSE from_id END) as person1,
    (CASE WHEN from_id > to_id THEN from_id ELSE to_id END) as person2, duration
    FROM Calls
)


SELECT 
    person1,
    person2,
    COUNT(duration) AS call_count ,
    SUM(duration) AS total_duration 
FROM Calls2
GROUP BY person1, person2;
