-- DELETE FROM Website_employee;
-- DELETE FROM Website_department;
-- DELETE FROM Website_training_program;
-- DELETE FROM Website_computer;
-- DELETE FROM Website_join_;
-- DELETE FROM Website_join;

-- DROP TABLE IF EXISTS Website_employee;
-- DROP TABLE IF EXISTS Website_department;
-- DROP TABLE IF EXISTS Website_training_program;
-- DROP TABLE IF EXISTS Website_computer;
-- DROP TABLE IF EXISTS Website_join_computer_employee;
-- DROP TABLE IF EXISTS Website_join_training_employee;

-- Employee --
INSERT into Website_employee VALUES (null, "Ousama", "Elayan", "2018-05-09", null, 0, 2);
INSERT into Website_employee VALUES (null, "Lesley", "Boyd", "2018-11-09", null, 0, 3);
INSERT into Website_employee VALUES (null, "Bryan", "Nilsen", "2018-06-02", null, 1, 5);
INSERT into Website_employee VALUES (null, "Elyse", "Dawson", "2018-10-01", null, 0, 5);
INSERT into Website_employee VALUES (null, "Rick", "Sanchez", "2019-01-28", "2019-01-28", 0, 1);
-- End Employee --

-- Department --
INSERT into Website_department VALUES (null, "Information Technology", 27500);
INSERT into Website_department VALUES (null, "Marketing", 150000);
INSERT into Website_department VALUES (null, "Management", 30000);
INSERT into Website_department VALUES (null, "Sales", 250000);
INSERT into Website_department VALUES (null, "Customer Service", 15000);
INSERT into Website_department VALUES (null, "Finance", 35000);
INSERT into Website_department VALUES (null, "Human Resources", 25000);
INSERT into Website_department VALUES (null, "Food Services", 100000);
-- End Department --

-- Training_Program --
INSERT into Website_training_program VALUES (null, "Newhire Orientation", "Onboard all company newhires. Basic day-to-day procedures and expectations will be covered. Orientation will be held in Conference Room 2 from 8am to 2pm.", "2019-01-25", "2019-01-25", 20);
INSERT into Website_training_program VALUES (null, "OSHA Safety Training", "Occupational Safety training is required for all Bangazon Employees. This program meets daily at 9am for 30 minutes.", "2019-02-12", "2019-02-16", 50);
INSERT into Website_training_program VALUES (null, "Effective Managing", "This program is for current and prospective managers to learn how to improve communication with subordinates. This program meets daily at 9am for 30 minutes.", "2019-02-12", "2019-02-16", 5);
INSERT into Website_training_program VALUES (null, "Social Media Guidelines", "This program will outline Bangazon's rules regarding the information employees may not post on various social media platforms. Training viewable online through company intranet. 2hrs.", "2019-02-18", "2019-02-18", 100);
INSERT into Website_training_program VALUES (null, "Admin Software Training", "Attendees will review how to use the online administration suite to manage Bangazon data. 3hrs.", "2019-03-15", "2019-03-15", 10);
INSERT into Website_training_program VALUES (null, "Training Training", "Attendees will be trained on how to train newhires. Training consists of training the trainers. 2hrs.", "2019-04-01", "2019-04-01", 10);
INSERT into Website_training_program VALUES (null, "Another Training Session", "Three-day training where attendees will be trained yet again. 1hr.", "2019-04-23", "2019-04-25", 50);
INSERT into Website_training_program VALUES (null, "Code of Conduct", "Two-day training where attendees will be trained on appropriate work behavior. 2hr.", "2019-05-14", "2019-05-15", 100);
-- End Training_Program --


-- Computer --
INSERT INTO Website_computer VALUES (null, "2018-02-01", null, "Lenovo", "Yoga 710", 0);
INSERT INTO Website_computer VALUES (null, "2019-01-01", null, "Apple", "15in MacBook Pro", 0);
INSERT INTO Website_computer VALUES (null, "2017-11-20", null, "Apple", "13in MacBook Air", 0);
INSERT INTO Website_computer VALUES (null, "2018-05-07", null, "Lenovo", "Thinkbook X1", 1);
INSERT INTO Website_computer VALUES (null, "2019-01-02", null, "Apple", "15in MacBook Pro", 0);
INSERT INTO Website_computer VALUES (null, "2019-01-03", null, "Apple", "15in MacBook Pro", 0);
INSERT INTO Website_computer VALUES (null, "2018-01-03", null, "Asus", "Aspire", 0);

-- End Computer --

-- Join_Training_Employee --
INSERT INTO Website_join_training_employee VALUES (null, 2, 1);
INSERT INTO Website_join_training_employee VALUES (null, 1, 3);
INSERT INTO Website_join_training_employee VALUES (null, 3, 2);
INSERT INTO Website_join_training_employee VALUES (null, 4, 6);
-- End Join_Training_Employee --

-- Join_Computer_Employee --
INSERT INTO Website_join_computer_employee VALUES(null, "2019-01-28", null, 1, 1);
INSERT INTO Website_join_computer_employee VALUES(null, "2018-12-25", null, 2, 2);
INSERT INTO Website_join_computer_employee VALUES(null, "2018-01-01", null, 3, 3);
INSERT INTO Website_join_computer_employee VALUES(null, "2018-05-04", null, 6, 4);
INSERT INTO Website_join_computer_employee VALUES(null, "2018-05-04", null, 5, 5);
INSERT INTO Website_join_computer_employee VALUES(null, "2018-11-09", "2019-01-27", 7, 1);

-- End Join_Employee_Computer --



