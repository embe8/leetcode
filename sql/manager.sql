# Given table: Find the manager with at least 5 direct 
#  Employee
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| id          | int     |
#| name        | varchar |
#| department  | varchar |
#| managerId   | int     |
#+-------------+---------+

SELECT id
FROM Employee e
JOIN (SELECT managerId
  FROM Employee e
  WHERE managerID IS NOT NULL
  GROUP BY managerID
  HAVING COUNT(managerId) >= 5
  ) m
ON e.id = m.managerId # e.id not e.managerId because we need to match id on Emmployee e table with managerId on m table
