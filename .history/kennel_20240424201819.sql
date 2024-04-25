CREATE TABLE `Location` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT NOT NULL,
  `address` TEXT NOT NULL
);

CREATE TABLE 'Customer' (
'id' INTEGER PRIMARY KEY AUTOINCREMENT,
'name' TEXT NOT NULL,
'address' TEXT NOT NULL,
'email' TEXT NOT NULL
);

CREATE TABLE 'Animal' (
'id' INTEGER PRIMARY KEY AUTOINCREMENT,
'name' TEXT NOT NULL,
'status' TEXT NOT NULL,
'breed' TEXT NOT NULL,
'customer_id' INTEGER NOT NULL,
'location_id' INTEGER,
FOREIGN KEY ('customer_id') REFERENCES 'Customer'('id'),
FOREIGN KEY ('location_id') REFERENCES 'Location'('id')
);

CREATE TABLE 'Employee' (
'id' INTEGER PRIMARY KEY AUTOINCREMENT,
'name' TEXT NOT NULL,
'address' TEXT NOT NULL,
'location_id' INTEGER NOT NULL,
FOREIGN KEY('location_id') REFERENCES 'Location'('id')
);

DROP TABLE IF EXISTS `Customers`;
DROP TABLE IF EXISTS `Locations`;

INSERT INTO `Location` VALUES (NULL, 'Nashville North', '64 Washington Heights');
INSERT INTO `Location` VALUES (NULL, 'Nashville South', '101 Penn Ave');

INSERT INTO `Employee` VALUES ('Madi Peper', '35498 Madison Ave', 1);
INSERT INTO `Employee` VALUES ('Kristen Norris', '100 Main St', 1);
INSERT INTO `Employee` VALUES ('Meg Ducharme', '404 Unknown Ct', 2);
INSERT INTO `Employee` VALUES ('Hannah Hall', '204 Empty Ave', 1);
INSERT INTO `Employee` VALUES ('Leah Hoefling', '200 Success Way', 2);

INSERT INTO `Customer` VALUES ('Mo Silvera', '201 Created St', 'mo@silvera.com', 'password');
INSERT INTO `Customer` VALUES ('Bryan Nilsen', '500 Internal Error Blvd', 'bryan@nilsen.com', 'password');
INSERT INTO `Customer` VALUES ('Jenna Solis', '301 Redirect Ave', 'jenna@solis.com', 'password');
INSERT INTO `Customer` VALUES ('Emily Lemmon', '454 Mulberry Way', 'emily@lemmon.com', 'password');

INSERT INTO `Animal` VALUES ('Snickers', 'Recreation', 'Dalmation', 4, 1);
INSERT INTO `Animal` VALUES ('Jax', 'Treatment', 'Beagle', 1, 1);
INSERT INTO `Animal` VALUES ('Falafel', 'Treatment', 'Siamese', 4, 2);
INSERT INTO `Animal` VALUES ('Doodles', 'Kennel', 'Poodle', 3, 1);
INSERT INTO `Animal` VALUES ('Daps', 'Kennel', 'Boxer', 2, 2);
INSERT INTO `Animal` VALUES ('Cleo', 'Kennel', 'Poodle', 2, 2);
INSERT INTO `Animal` VALUES ('Popcorn', 'Kennel', 'Beagle', 3, 2);
INSERT INTO `Animal` VALUES ('Curly', 'Treatment', 'Poodle', 4, 2);
