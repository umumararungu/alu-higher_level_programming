-- california cities
SELECT name.cities from cities,states ON state.id=cities.id WHERE states.name='Calfornia';
