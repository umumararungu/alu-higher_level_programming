-- california cities
SELECT id,name FROM cities WHERE states_id=( SELECT id FROM states WHERE name='Calfornia') ORDER BY id;
