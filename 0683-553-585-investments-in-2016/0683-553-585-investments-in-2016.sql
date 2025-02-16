# Write your MySQL query statement below
-- Write your PostgreSQL query statement below
-- SELECT
--     ROUND(SUM(tiv_2016):: DECIMAL, 2) AS tiv_2016
-- FROM Insurance
-- WHERE 
--     tiv_2015 IN(
--         SELECT tiv_2015 
--         FROM Insurance
--         GROUP BY tiv_2015
--         HAVING COUNT(*) > 1
--     )
-- AND
--     CONCAT(lat, lon) IN(
--         SELECT CONCAT(lat, lon)
--         FROM Insurance
--         GROUP BY lat, lon
--         HAVING COUNT(*) = 1
--     );

# WITH cte AS(
#     SELECT
#         tiv_2016,
#         COUNT(*) OVER(PARTITION BY lat, lon) AS city_count,
#         COUNT(*) OVER(PARTITION BY tiv_2015) AS tiv_count
#         FROM 
#             Insurance
# )

# SELECT 
#     ROUND(SUM(tiv_2016):: DECIMAL, 2) AS tiv_2016
# FROM 
#     cte
# WHERE
#     city_count = 1
# AND 
#     tiv_count>1;
WITH cte AS(
    SELECT
        tiv_2016,
        COUNT(*) OVER(PARTITION BY lat, lon) AS city_count,
        COUNT(*) OVER(PARTITION BY tiv_2015) AS tiv_count
        FROM 
            Insurance
)

SELECT 
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM 
    cte
WHERE
    city_count = 1
AND 
    tiv_count>1;