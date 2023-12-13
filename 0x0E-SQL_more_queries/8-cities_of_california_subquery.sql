-- This is a script that lists all the cities of californa
-- that can not be found in the database
USE hbtn_0d_usa;

SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
  AND states.name = 'California'
ORDER BY cities.id ASC;
