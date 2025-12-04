'''Problem name: Monthly Transactions I
Given the following table:
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
Find: Query that returns the following--for each month and country, 
the number of transactions and their total amount, the number of 
approved transactions and their total amount
Expected output:
| month   | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
| ------- | ------- | ----------- | -------------- | ------------------ | --------------------- |
| 2018-12 | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01 | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01 | DE      | 1           | 1              | 2000               | 2000                  |
'''

# Write your MySQL query statement below
SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month, 
    country, 
    COUNT(*) as trans_count, 
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) as approved_count, 
    SUM(amount) as trans_total_amount, 
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) as approved_total_amount
FROM 
    Transactions
GROUP BY 
    DATE_FORMAT(trans_date, '%Y-%m'),
    country
