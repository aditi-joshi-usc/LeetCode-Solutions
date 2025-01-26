# Write your MySQL query statement below
select Visits.customer_id, COUNT(*) as count_no_trans
from Visits 
where Visits.visit_id not in (select visit_id from Transactions) 
group by customer_id;