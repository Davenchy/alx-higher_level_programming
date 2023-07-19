-- create the hbtn_0d_2 database
CREATE DATABASE hbtn_0d_2;
-- create the user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant SELECT privilege to the user user_0d_2 only on the hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
