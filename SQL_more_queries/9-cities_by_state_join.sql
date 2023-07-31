-- cities and states
SELECT cities.id AS id,cities.name AS name,states.name AS name FROM cities FULL JOIN states ORDER BY id ASC;
