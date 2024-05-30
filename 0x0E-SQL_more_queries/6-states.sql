-- database hbtn_0d_usa and table states on your MySQL server is created
-- database is created
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- uses database
USE hbtn_0d_usa;
-- creates table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
