INSERT INTO dojos (name)
VALUES ("Dallas"), ("Little Rock"), ("Fayetville");

SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("John", "Browne", 34, 4), ("Acle", "Kahney", 36, 4), ("Olly", "Steele", 31, 4), 
	("Andy", "Cizek", 27, 5), ("Daniel", "Tompkins", 36, 5), ("Adam", "Benjamin", 31, 5),
    ("Mike", "Malyan", 34, 6), ("Jay", "Postones", 36, 6), ("Jordan", "Henderson", 26, 6);

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo.id
WHERE dojos.id = 4;

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo.id
WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);
