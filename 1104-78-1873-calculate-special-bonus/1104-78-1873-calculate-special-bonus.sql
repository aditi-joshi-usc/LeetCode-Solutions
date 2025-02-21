# Write your MySQL query statement below
select employee_id, 
(case 
when employee_id % 2 !=0 and left(name,1) != 'M' THEN  salary
else 0
end) as 
bonus
from Employees
ORDER BY employee_id;