-- A script that lists all cities contained in the database hbtn_0d_usa
-- Results will be sorted in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.states_id = states.id;
