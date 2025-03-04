# Write your MySQL query statement below
with cte as(
    select distinct user2_id as user_id from Friendship where user1_id = 1
    UNION
    select distinct user1_id as user_id from Friendship where user2_id = 1
)

select distinct page_id as recommended_page from Likes 
where user_id != 1 and user_id in (select user_id from cte) 
and page_id not in(select page_id from Likes where user_id = 1);