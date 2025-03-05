# Write your MySQL query statement below
-- WITH cte as(
--     SELECT Wimbledon as id, COUNT(*) as cnt FROM Championships GROUP BY Wimbledon
--     UNION ALL
--     SELECT Fr_open as id, COUNT(*) as cnt FROM Championships GROUP BY Fr_open 
--     UNION ALL
--     SELECT US_open  as id, COUNT(*) as cnt FROM Championships GROUP BY US_open  
--     UNION ALL
--     SELECT Au_open as id, COUNT(*) as cnt FROM Championships GROUP BY Au_open 
-- )

-- SELECT c.id as player_id, p.player_name, SUM(cnt) as grand_slams_count 
-- FROM cte AS c LEFT JOIN Players AS p
-- ON c.id = p.player_id
-- GROUP BY c.id;


SELECT p.player_id, p.player_name,
(SUM(p.player_id = Wimbledon)+SUM(p.player_id = Fr_open )+SUM(p.player_id = US_open )+SUM(p.player_id = Au_open )) as grand_slams_count 
FROM Players AS p
INNER JOIN 
Championships
ON p.player_id = Wimbledon or p.player_id = Fr_open  or p.player_id =US_open or p.player_id = Au_open
GROUP BY p.player_id;