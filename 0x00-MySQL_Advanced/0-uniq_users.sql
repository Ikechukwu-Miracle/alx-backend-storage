-- A script that creates a table users for any database

CREATE TABLE IF NOT EXISTs users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
 