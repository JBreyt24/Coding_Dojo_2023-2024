INSERT INTO users (first_name, last_name, email)
VALUES ("John", "Browne", "browneuments@gmail.com"),
("Acle", "Kahney", "4Dstudios@gmail.com"),
("Olly", "Steele", "OliverSteele@gmail.com");

SELECT * FROM users;

SELECT * FROM users
WHERE email = "browneuments@gmail.com";

SELECT * FROM users
WHERE id = 3;

UPDATE users SET last_name = "Pancakes"
WHERE users.id = 3;

DELETE FROM users
WHERE users.id = 2;

SELECT * FROM users
ORDER BY first_name;

SELECT * FROM users
ORDER BY first_name DESC;