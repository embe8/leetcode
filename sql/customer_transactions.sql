'''Problem: Given Table Visits where visit ID has the unique entries and Table Transactions where Transaction id has the unique values,
create query that outputs all customers ID who have not made a single transaction during their visits. Also output the total number of these kinds of visits for each customer in any order'''

SELECT v.customer_id, COUNT(v.customer_id) as no_transaction_visits
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.visit_id is NULL
GROUP BY v.customer_id

'''Note: after LEFT JOIN visits v to transactions t, all entries in transactions t that has no match with visits ID meaning all customers that made no transactions are left with null in t.visit_id'''
'''Note: for left join all transactions in left table are included'''
