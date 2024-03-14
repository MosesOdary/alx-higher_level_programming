-- lists all cities of California that found in the database
-- lists all rows for column in the database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
