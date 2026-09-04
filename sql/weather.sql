# RISING TEMPERATURE
# Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

SELECT today.id
FROM Weather yesterday
# difference between date 1 and date 2 should be 1
# and temperature in 
CROSS JOIN Weather today# join with itself
