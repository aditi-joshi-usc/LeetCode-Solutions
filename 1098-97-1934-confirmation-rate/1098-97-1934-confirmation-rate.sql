SELECT sign.user_id, 
ROUND(AVG(CASE
WHEN action = "confirmed" THEN 1
ELSE 0
END),2)  as confirmation_rate
 FROM
Signups sign LEFT JOIN Confirmations con ON sign.user_id = con.user_id
group by user_id;