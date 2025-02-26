# Write your MySQL query statement below
select users.name,
    SUM(Transactions.amount) as balance
FROM Transactions
JOIN Users
ON Users.account = Transactions.account
GROUP BY users.name
HAVING balance > 10000; 