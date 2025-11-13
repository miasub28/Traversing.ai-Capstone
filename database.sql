-- database.sql
-- Create a table that contains exactly one row with the single value "hello world"

CREATE TABLE hello_world (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    message TEXT NOT NULL CHECK (message = 'hello world')
);

INSERT INTO hello_world (id, message) VALUES (1, 'hello world');