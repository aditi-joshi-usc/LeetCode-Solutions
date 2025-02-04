# Write your MySQL query statement below
DELETE p
FROM Person p
JOIN Person s ON p.email = s.email
WHERE p.id > s.id;

