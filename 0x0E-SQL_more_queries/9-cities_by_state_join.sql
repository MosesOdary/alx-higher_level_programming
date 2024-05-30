-- lists all cities contained in database
-- lists all rows for particular column in the database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
