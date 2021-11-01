CREATE DATABASE `SSIS`;

USE `SSIS`;

CREATE TABLE `College` (
    `code` VARCHAR(10) NOT NULL,
    `name` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`code`)
);

CREATE TABLE `Course` (
    `code` VARCHAR(10) NOT NULL,
    `name` VARCHAR(50) NOT NULL,
    `college` VARCHAR(10) NOT NULL,
    PRIMARY KEY (`code`), 
    FOREIGN KEY (`college`) REFERENCES `College` (`code`)
);

CREATE TABLE `Student` (
    `id` CHAR(9) NOT NULL,
    `first_name` VARCHAR(50) NOT NULL,
    `middle_name` VARCHAR(50) NOT NULL,
    `last_name` VARCHAR(50) NOT NULL,
    `course` VARCHAR(10) NOT NULL,
    `year` INTEGER NOT NULL,
    `birth_date` DATE NOT NULL,
    `birth_place` VARCHAR(75) NOT NULL,
    `sex` VARCHAR(6) NOT NULL,
    `gender` VARCHAR(20) NOT NULL, 
    `civil_status`VARCHAR(10) NOT NULL,
    `citizenship` VARCHAR(20) NOT NULL,
    `address` VARCHAR(75) NOT NULL,
    `contact_number` VARCHAR(15) NOT NULL,
    `image_url` varchar(255),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`course`) REFERENCES `Course` (`code`)
);
