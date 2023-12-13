-- This is a script that lists all the cities of californa
-- that can not be found in the database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
