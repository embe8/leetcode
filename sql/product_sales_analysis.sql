'''Given the following tables: SALES table
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
  and PRODUCT table
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+ make a query that shows Product_name, price and year for each sale_id in Sales table
'''

SELECT product_name, price, year
FROM SALES s
INNER JOIN PRODUCT p 
ON p.product_id = s.product_id
