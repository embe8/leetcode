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
# mySQL only: for postgres it throws an error
SELECT a.machine_id,
round(
    (SELECT avg(a1.timestamp) from Activity a1 where a1.activity_type='end' and a1.machine_id = a.machine_id) -
    (SELECT avg(a1.timestamp) from Activity a1 where a1.activity_type='start' and a1.machine_id = a.machine_id
    ), 3) as processing_time
from Activity a
GROUP BY a.machine_id
# PostGres solution:
SELECT  machine_id,
        ROUND(
            AVG(
            CASE 
                WHEN activity_type = 'start' THEN -timestamp 
                ELSE timestamp
            END)::decimal * 2 # there are two rows per process_id
            , 3) AS processing_time
FROM Activity
GROUP BY machine_id
ORDER BY machine_id ASC;

# for Postgresql ROUND alone invalid use this:
SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp)::numeric, 3) AS processing_time
FROM Activity a1
JOIN Activity a2
  ON a1.machine_id = a2.machine_id
  AND a1.process_id = a2.process_id
  AND a1.activity_type = 'start'
  AND a2.activity_type = 'end'
GROUP BY a1.machine_id
ORDER BY processing_time ASC
