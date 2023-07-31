-- check privileges
SHOW GRANTS FOR 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH auntentication_plugin BY 'password1';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED WITH auntentication_plugin BY 'password2';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
