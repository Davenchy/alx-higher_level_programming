-- creates a new table if only not exists and add some records
-- create the database only if not exists with fields: id, name and score
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- add John record
INSERT INTO second_table VALUES (1, "John", 10);
-- add Alex record
INSERT INTO second_table VALUES (2, "Alex", 3);
-- add Bob record
INSERT INTO second_table VALUES (3, "Bob", 14);
-- add George record
INSERT INTO second_table VALUES (4, "George", 8);
