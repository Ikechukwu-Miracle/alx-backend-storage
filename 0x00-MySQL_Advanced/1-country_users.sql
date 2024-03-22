-- A script that creates a table users for any database

CREATE TABLE IF NOT EXIST users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id)
);
