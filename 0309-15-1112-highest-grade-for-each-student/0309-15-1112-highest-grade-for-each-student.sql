# Write your MySQL query statement below
WITH cte AS(SELECT 
    student_id, course_id, grade, RANK() OVER(PARTITION BY student_id ORDER BY grade desc, course_id asc) as rank_val
FROM Enrollments )

SELECT student_id, course_id, grade 
FROM cte 
WHERE rank_val = 1;

