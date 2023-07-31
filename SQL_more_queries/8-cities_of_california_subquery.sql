-- california cities
SELECT states.id,cities.id,cities.name FROM cities,states ON cities.id=states.id WHERE states.id=( SELECT id FROM states WHERE name='Calfornia') ORDER BY cities.id ASC;
