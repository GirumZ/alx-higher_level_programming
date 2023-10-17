-- A script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- hbtn_0c_0 is given
SELECT city, AVG(value) AS avg_temp
FROM tempratures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
