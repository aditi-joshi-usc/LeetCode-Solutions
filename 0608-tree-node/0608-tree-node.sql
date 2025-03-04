# Write your MySQL query statement below
select id, (
    CASE 
    WHEN p_id is NULL THEN 'Root'
    WHEN id IN (SELECT DISTINCT p_id FROM Tree) THEN 'Inner'
    ELSE 'Leaf'
    END
) AS type
FROM Tree;