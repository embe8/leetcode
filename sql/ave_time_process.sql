+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
# Problem name: Average Time of Process Per Machine
# Problem: There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.

SELECT a.machine_id,
round(
    (SELECT avg(a1.timestamp) from Activity a1 where a1.activity_type='end' and a1.machine_id = a.machine_id) -
    (SELECT avg(a1.timestamp) from Activity a1 where a1.activity_type='start' and a1.machine_id = a.machine_id
    ), 3) as processing_time
from Activity a
GROUP BY a.machine_id
