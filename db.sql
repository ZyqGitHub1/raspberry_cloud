--
-- File generated with SQLiteStudio v3.0.6 on 周二 4月 12 01:45:08 2016
--
-- Text encoding used: GBK
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: roles
CREATE TABLE roles (
	id INTEGER NOT NULL, 
	name VARCHAR(64), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);

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

-- Table: users
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(64), 
	email VARCHAR(64), 
	role_id INTEGER, 
	password_hash VARCHAR(128), 
	confirmed BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(role_id) REFERENCES roles (id), 
	CHECK (confirmed IN (0, 1))
);
INSERT INTO users (id, username, email, role_id, password_hash, confirmed) VALUES (1, '张永钦', '1559650514@qq.com', NULL, 'pbkdf2:sha1:1000$uZwcyoQw$8a3f41f7088cb736f69c0e66768da3ba375ef0a9', 0);
INSERT INTO users (id, username, email, role_id, password_hash, confirmed) VALUES (2, '程豪', '940068139@qq.com', NULL, 'pbkdf2:sha1:1000$ffFae3aT$1def80ea4720f9924312815652de61c4d46d285f', 1);
INSERT INTO users (id, username, email, role_id, password_hash, confirmed) VALUES (3, 'znx', 'qqdhsy@126.com', NULL, 'pbkdf2:sha1:1000$6NaEzgux$46144c03a6f588baafb0626fddfc7189feccd0f9', 1);

-- Table: alembic_version
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL
);

-- Table: electricals
CREATE TABLE electricals (
	id INTEGER NOT NULL, 
	electname VARCHAR(64), 
	pin_id INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (electname), 
	FOREIGN KEY(pin_id) REFERENCES pin (id)
);

-- Index: ix_users_email
CREATE UNIQUE INDEX ix_users_email ON users (email);

-- Index: ix_users_username
CREATE UNIQUE INDEX ix_users_username ON users (username);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
