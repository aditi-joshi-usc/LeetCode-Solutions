# Write your MySQL query statement below
-- SELECT DISTINCT a.account_id
-- FROM LogInfo AS a 
-- JOIN LogInfo AS b
-- ON a.account_id = b.account_id
-- AND a.ip_address != b.ip_address
-- AND(
-- a.login BETWEEN b.login and b.logout
-- or a.logout  BETWEEN b.login and b.logout);

SELECT DISTINCT a.account_id
FROM LogInfo AS a 
JOIN LogInfo AS b
ON a.account_id = b.account_id
AND a.ip_address != b.ip_address
AND a.login <= b.logout
AND b.login <= a.logout;