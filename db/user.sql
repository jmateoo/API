CREATE DATABASE migrate_db;
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON `migrate_db` . * TO 'user'@'localhost';
FLUSH PRIVILEGES; 