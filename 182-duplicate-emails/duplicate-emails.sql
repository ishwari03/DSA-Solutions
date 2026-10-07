SELECT email as EMAIL
FROM Person 
GROUP BY email
HAVING COUNT(email) >1