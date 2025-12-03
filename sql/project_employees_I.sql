# Project employees I 
# Given table project that shows employee ID and project ID and another table named employees 
# showing employee IDa, name and experience in years, the common PK for both is employee ID

# Problem: Find the average number of years each employee has worked in each project

SELECT project_id, ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY p.project_id
