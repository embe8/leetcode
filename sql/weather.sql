# RISING TEMPERATURE
# Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

SELECT today.id
FROM Weather yesterday
# difference between date 1 and date 2 should be 1
# and temperature in 
CROSS JOIN Weather today# join with itself

#alternate solution joins table with itself
SELECT w1.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature;

#
#Join the Weather table with itself, denoting the first occurrence as w1 and the second occurrence as w2.
#Compare the dates of w1 and w2 using the DATEDIFF() function to check if they are consecutive days (with a difference of 1 day).
#Add a condition in the WHERE clause to select the rows where the temperature of w1 is greater than the temperature of w2.
#Select the id of w1 as the result.
