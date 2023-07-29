-- check privileges
CREATE USER 'user_0d_1'@'localhost','user_0d_2'@'localhost';
GRANT ALL privileges ON *.* TO 'user_0d_1'@'localhost','user_0d_2'@'localhost';
