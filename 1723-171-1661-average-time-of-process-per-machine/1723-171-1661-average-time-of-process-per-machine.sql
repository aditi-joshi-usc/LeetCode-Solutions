# Write your MySQL query statement below
select machine_id, round(avg(sum_value),3) as processing_time from 
(
select machine_id, sum(if(activity_type = 'end',1,-1 )*timestamp) as sum_value 
from Activity
group by machine_id, process_id
) as sum_value_query
group by machine_id;