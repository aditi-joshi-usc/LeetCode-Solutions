#-- Write your PostgreSQL query statement below
-- WITH cte AS (
--     SELECT visited_on, SUM(amount) AS sum_amt
--     FROM Customer
--     GROUP BY visited_on
-- )

-- SELECT visited_on, SUM(sum_amt) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
-- ROUND(AVG(sum_amt) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS average_amount
-- FROM cte
-- ORDER BY visited_on
-- OFFSET 6 ROWS;

# Write your MySQL query statement below
# Write your MySQL query statement below
WITH t1 AS (SELECT customer_id,visited_on,SUM(amount)AS amount
             FROM Customer
             GROUP BY visited_on),
t AS (SELECT visited_on,SUM(amount) OVER (ORDER BY visited_on ASC
                                           RANGE BETWEEN INTERVAL '6' DAY PRECEDING AND CURRENT ROW ) AS amount,
            ROUND(AVG(SUM(amount)) OVER (ORDER BY visited_on ASC
                                          RANGE BETWEEN INTERVAL '6' DAY PRECEDING AND CURRENT ROW ),2) AS average_amount
            FROM t1
            GROUP BY visited_on)
SELECT * 
FROM t
WHERE visited_on >= (SELECT MIN(visited_on) FROM t)+INTERVAL 6 DAY 