# Write your MySQL query statement below
-- SELECT id, CASE
--     WHEN id % 2 = 0  THEN LAG(student) OVER(ORDER BY id)
--     ELSE COALESCE(LEAD(student) OVER(ORDER BY id), student)
--     END as student
-- FROM Seat;

SELECT CASE 
    WHEN id = (SELECT MAX(id) FROM Seat) AND id % 2 = 1 THEN id
    WHEN id % 2 = 1 THEN id + 1
    ELSE  id - 1
END AS id, student
FROM Seat
ORDER BY id;
