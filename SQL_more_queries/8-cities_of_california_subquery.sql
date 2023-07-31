-- california cities
SELECT cities.name,cities.id FROM cities,states ON state.id=cities.id WHERE states.name='Calfornia';
