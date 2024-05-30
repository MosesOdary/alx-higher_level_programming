-- creates database hbtn_0d_2 & user user_0d_2
-- creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grants privileges to user <SELECT>
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
