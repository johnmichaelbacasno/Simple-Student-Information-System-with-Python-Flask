USE `SSIS`;

/*Courses*/

INSERT INTO `College`(`code`, `name`)
VALUES('CCS', 'College of Computer Studies');

/*Courses*/

INSERT INTO `Course`(`code`, `name`, `college`)
VALUES('BSCS', 'Bachelor of Science in Computer Science', 'CCS');

INSERT INTO `Course`(`code`, `name`, `college`)
VALUES('BSIT', 'Bachelor of Science in Information Technology', 'CCS');

INSERT INTO `Course`(`code`, `name`, `college`)
VALUES('BSCA', 'Bachelor of Science in Computer Applications', 'CCS');

INSERT INTO `Course`(`code`, `name`, `college`)
VALUES('BSIS', 'Bachelor of Science in Information System', 'CCS');

/*Students*/

INSERT INTO `Student`(`id`, `first_name`, `middle_name`, `last_name`, `course`, `year`, `birth_date`, `birth_place`, `sex`, `gender`, `civil_status`, `citizenship`, `address`, `contact_number`, `image_url`)
VALUES('2000-0001', 'Kyle', 'Evan', 'Sebastian', 'BSCS', 3, '2000-07-18', 'Quezon City', 'Male', 'Heterosexual', 'Single', 'Filipino', 'Quezon City', '09000000000', 'https://res.cloudinary.com/johnmichaelbacasno/image/upload/ssis/student_images/2000-0001.jpg');