with t1 as (
select 
caller_id,
cy.name,
c.duration
from Calls c
left join Person p on c.caller_id=p.id
left join Country cy on cy.country_code=left(p.phone_number,3)),

t2 as (
select 
callee_id,
cy.name,
c.duration
from Calls c
left join Person p on c.callee_id=p.id
left join Country cy on cy.country_code=left(p.phone_number,3)
),

t3 as (
select 
name,duration
from t1
union all
select 
name,duration
from t2
),

avg_per_country as (
select
name,
avg(duration) as avg_per_country
from t3
group by name),
avg_global as(
    select
    avg(duration) as aglobal
    from t3
)

select name as country
from avg_per_country, avg_global
where avg_per_country>aglobal