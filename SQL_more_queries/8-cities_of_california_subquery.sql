-- california cities
SELECT id,name FROM cities WHERE states_id=( SELECT id FROM states WHERE name='Calfornia') and id=state_id ORDER BY id;
