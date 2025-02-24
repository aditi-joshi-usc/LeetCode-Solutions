# Write your MySQL query statement below
WITH cte as(
    select
        *
    from  teams
    left join matches
    on teams.team_id = matches.host_team or teams.team_id = matches.guest_team
)

select team_id, team_name,
SUM(   
    CASE
        WHEN team_id = host_team and host_goals>guest_goals THEN 3
        WHEN team_id = guest_team and host_goals < guest_goals THEN 3  
        WHEN team_id = host_team and host_goals=guest_goals THEN 1
        WHEN team_id = guest_team and host_goals=guest_goals THEN 1
        ELSE 0
    END
) AS num_points
FROM cte
GROUP BY team_id
ORDER BY num_points DESC, team_id ASC;