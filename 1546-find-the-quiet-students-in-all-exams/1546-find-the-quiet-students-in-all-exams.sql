# Write your MySQL query statement below




WITH ranking AS(
    SELECT student_id,
    RANK() OVER(PARTITION BY exam_id ORDER BY score ASC) AS grade
    FROM EXAM
    UNION ALL
    SELECT student_id,
    RANK() OVER(PARTITION BY exam_id ORDER BY score DESC) AS grade
    FROM Exam
)

SELECT * FROM Student where student_id
NOT IN (SELECT DISTINCT student_id FROM ranking WHERE grade =1) AND student_id in (SELECT student_id FROM Exam) ORDER BY student_id; 