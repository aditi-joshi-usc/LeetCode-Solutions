# Write your MySQL query statement below
select a.id from Weather a
cross join Weather b
where datediff(a.recordDate, b. recordDate) = 1 and a.temperature > b.temperature;