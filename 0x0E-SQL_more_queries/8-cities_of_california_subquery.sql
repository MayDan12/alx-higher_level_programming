-- This is a script that lists all the cities of californa
-- that can not be found in the database
USE hbtn_0d_usa;

SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY cities.id ASC;
