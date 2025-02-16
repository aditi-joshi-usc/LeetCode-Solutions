# Write your MySQL query statement below

-- WITH helper AS
-- (
--     SELECT 
--         E.name Employee, 
--         E.salary Salary,
--         D.name Department,
--         DENSE_RANK() OVER (PARTITION BY D.id ORDER BY salary DESC) rank
--     FROM Employee E INNER JOIN Department D
--     ON D.id = E.departmentId
-- )


-- SELECT 
--     Employee, 
--     Salary,
--     Department
-- FROM helper
-- WHERE rank < 4;


SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM
    Employee e
    JOIN Department d ON e.departmentId = d.id
WHERE
    (
        SELECT COUNT(DISTINCT salary)
        FROM Employee e2
        WHERE e2.departmentId = e.departmentId AND e2.salary >= e.salary
    ) <= 3
ORDER BY
    Department, Salary DESC;