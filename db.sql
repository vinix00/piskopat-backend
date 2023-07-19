DROP DATABASE piskodb;
CREATE DATABASE piskodb;
USE piskodb;

CREATE TABLE users (
  uid INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(45) NOT NULL,
  password VARCHAR(45) NOT NULL,
  join_date DATE NOT NULL,
  role INT NOT NULL,
  PRIMARY KEY(uid)
);

CREATE TABLE invite_codes (
  invite_id INT NOT NULL AUTO_INCREMENT,
  code VARCHAR(45) NOT NULL,
  PRIMARY KEY(invite_id)
);






CREATE TABLE IF NOT EXISTS `mydb`.`invtes` (
  `invite_id` INT NOT NULL,
  `invite_code` VARCHAR(45) COLLATE 'DEFAULT' NOT NULL,
  `creator_id` INT NOT NULL,
  PRIMARY KEY (`invite_id`),
  UNIQUE INDEX `invite_code_UNIQUE` (`invite_code` ASC) VISIBLE)
ENGINE = InnoDB

CREATE TABLE IF NOT EXISTS `mydb`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `join_date` DATE NOT NULL,
  `inviter_id` INT NULL,
  INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  CONSTRAINT `user_id`
    FOREIGN KEY ()
    REFERENCES `mydb`.`invtes` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB