-- create hbtn_0d_usa database only if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create states table only if not exists with id as a primary key and name columns
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL REFERENCES hbtn_0d_usa.states (id),
	name VARCHAR(256) NOT NULL
);
