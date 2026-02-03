'''Name: Replace Employee ID with unique identifier
Problem: Given the following tables: 
Table: Employees

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+

EmployeeUNI

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+ where the PK for both tables is ID, create query that outputs the unique ID for every employee, those with none should be shown as NULL (any order)
'''

SELECT unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id
