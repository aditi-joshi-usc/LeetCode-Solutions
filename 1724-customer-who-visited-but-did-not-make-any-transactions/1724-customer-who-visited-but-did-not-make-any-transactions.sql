# Write your MySQL query statement below
-- select Visits.customer_id, COUNT(*) as count_no_trans
-- from Visits 
-- where Visits.visit_id not in (select visit_id from Transactions) 
-- group by customer_id;

select visits.customer_id, count(*) as count_no_trans 
from 
    visits
left join
    transactions as t
on visits.visit_id = t.visit_id
where t.transaction_id is null
group by visits.customer_id;