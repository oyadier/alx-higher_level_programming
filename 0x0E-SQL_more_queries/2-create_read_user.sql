-- create db and user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXIST user_0d_2;
GRANT SELECT ON *.* 'user_0d_2'@'localhost';
