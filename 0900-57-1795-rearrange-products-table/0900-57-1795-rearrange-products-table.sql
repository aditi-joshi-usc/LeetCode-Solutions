# Write your MySQL query statement below
with cte as(
SELECT
  product_id, 'store1' AS store, 
  (
    CASE WHEN store1 IS NOT NULL THEN store1 ELSE NULL END
  ) AS price
FROM Products
WHERE store1 IS NOT NULL
  UNION 
SELECT
  product_id, 'store2' AS store,
  (
    CASE WHEN store2 IS NOT NULL THEN store2 ELSE NULL END
  ) AS price
FROM Products
WHERE store2 IS NOT NULL
UNION 
SELECT
  product_id, 'store3' AS store,
  (
    CASE WHEN store3 IS NOT NULL THEN store3 ELSE NULL END
  ) AS price
FROM Products
WHERE store3 IS NOT NULL
)

Select * from cte;


-- SELECT product_id, store, price
-- FROM
-- (SELECT product_id, unnest(array['store1', 'store2', 'store3']) as store, unnest(array[store1, store2, store3]) as price From Products ) AS subq
-- WHERE price is not null
