-- cities and states
SELECT cities.id as id,cities.name as name,states.name as name FROM cities FULL JOIN states ORDER BY cities.id ASC;
