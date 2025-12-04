'''Problem name: Queries Quality and Percentage
Given table named queries:
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
Find: the query that returns query name, quality (rating:position ratio)
and poor_quality_Rating (queries with less than 3 quality)'''

SELECT 
    query_name, 
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS poor_query_percentage
FROM 
    Queries
GROUP BY 
    query_name
