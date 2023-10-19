-- A script that creates the database hbtn_0d_usa and the table cities
-- Create the database
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
--Create table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES state(id));
