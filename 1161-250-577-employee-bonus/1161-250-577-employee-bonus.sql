# Write your MySQL query statement below
select name, bonus 
from Employee emp LEFT JOIN Bonus bon ON emp.empId = bon.empId
where bon.bonus<1000 or bon.bonus is null;  
