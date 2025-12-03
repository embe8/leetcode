# Problem name: Percentage of Users Attended A contest
# Given Table 1 named users with user_id and user_name and Table 2
# named Register with contest_id and user_id and user_id being the PK for both,
# Problem: Find the percentage of users for each contest rounded to 2 decimal places

SELECT contest_id, (AVG(user_id) / SUM(user_id) as percentage_user
FROM Users u
JOIN Register r
ON u.user_id = r.user_id
GROUP BY r.contest_id
