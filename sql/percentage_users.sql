# Problem name: Percentage of Users Attended A contest
# Given Table 1 named users with user_id and user_name and Table 2
# named Register with contest_id and user_id and user_id being the PK for both,
# Problem: Find the percentage of users for each contest rounded to 2 decimal places

SELECT 
    contest_id,
    ROUND(COUNT(user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
GROUP BY 
    contest_id
ORDER BY
    percentage DESC,
    contest_id ASC
