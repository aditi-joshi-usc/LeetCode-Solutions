# Write your MySQL query statement below
-- with cte as (
--     select abs(p1.x - p2.x) as dist
--     from Point AS p1 JOIN Point AS p2 ON p1.x != p2.x
-- )

-- SELECT MIN(dist) AS shortest from cte;

with cte as(
   select x, LAG(x,1) OVER(ORDER BY x) as prev,x - LAG(x) OVER(ORDER BY x) as diff
    from Point
)
select MIN(diff) as shortest from cte;
