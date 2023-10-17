-- A script that displays the max temperature of each state
-- hbtn_0c_0 is given
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state
LIMIT 3;
