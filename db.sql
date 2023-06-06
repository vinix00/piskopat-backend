DROP DATABASE piskodb;
CREATE DATABASE piskodb;
USE piskodb;

CREATE TABLE user (
  uid INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(45) NOT NULL,
  password VARCHAR(45) NOT NULL,
  created_at DATE NOT NULL,
  role INT NOT NULL,
  PRIMARY KEY(uid)
);