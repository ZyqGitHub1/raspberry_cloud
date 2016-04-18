--
-- File generated with SQLiteStudio v3.0.6 on ÖÜ¶þ 4ÔÂ 12 01:41:34 2016
--
-- Text encoding used: GBK
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: pin
CREATE TABLE pin (
	id INTEGER NOT NULL, 
	bcm_id INTEGER, 
	wpi_id INTEGER, 
	useable BOOLEAN, 
	state BOOLEAN, 
	PRIMARY KEY (id), 
	UNIQUE (bcm_id), 
	UNIQUE (wpi_id), 
	CHECK (useable IN (0, 1)), 
	CHECK (state IN (0, 1))
);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (1, NULL, NULL, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (2, NULL, NULL, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (3, 2, 8, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (4, NULL, NULL, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (5, 3, 9, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (6, NULL, NULL, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (7, 4, 7, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (8, 14, 15, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (9, NULL, NULL, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (10, 15, 16, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (11, 17, 0, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (12, 18, 1, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (13, 27, 2, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (14, NULL, NULL, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (15, 22, 3, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (16, 23, 4, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (17, NULL, NULL, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (18, 24, 5, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (19, 10, 12, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (20, NULL, NULL, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (21, 9, 13, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (22, 25, 6, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (23, 11, 14, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (24, 8, 10, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (25, NULL, NULL, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (26, 7, 11, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (27, 0, 30, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (28, 1, 31, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (29, 5, 21, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (30, NULL, NULL, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (31, 6, 22, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (32, 12, 26, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (33, 13, 23, 1, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (34, NULL, NULL, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (35, 19, 24, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (36, 16, 27, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (37, 26, 25, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (38, 20, 28, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (39, NULL, NULL, 0, 0);
INSERT INTO pin (id, bcm_id, wpi_id, useable, state) VALUES (40, 21, 29, 1, 0);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
