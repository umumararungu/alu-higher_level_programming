-- california cities
SELECT states.id,cities.id,cities.name FROM cities,states WHERE states.id=( SELECT id FROM states WHERE name='Calfornia') and cities.id=states.id ORDER BY cities.id;
