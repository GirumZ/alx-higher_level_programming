-- A script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- hbtn_0c_0 is given
SELECT city, AVG(value) AS avg_temp
FROM tempretures
GROUP BY city
ORDER BY avg_temp DESC;
