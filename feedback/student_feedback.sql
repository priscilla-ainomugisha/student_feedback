-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 07, 2023 at 11:47 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_feedback`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$6VhN7qYyh7WlnG3q2y91wL$sag3EKNgR44vgrQ5VlWauKnzUkQnVxLg7RCO906njjI=', NULL, 0, 'priscilla', '', '', 'ainomugishapriscilla00@gmail.com', 0, 1, '2023-08-07 06:11:04.754533'),
(2, 'pbkdf2_sha256$600000$Drwcz8gBubbKIwRlfsBWTT$4Jwnas8oprzx6/kG6gK+63wnzAm/fMvTl2R6w2SWX0c=', NULL, 0, 'ainomugisha.priscilla', '', '', 'ainomugishapriscilla00@gmail.com', 0, 1, '2023-08-07 07:03:40.792458');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `course_info`
--

CREATE TABLE `course_info` (
  `CODE` varchar(10) DEFAULT NULL,
  `COURSE_NAME` varchar(100) DEFAULT NULL,
  `CU` int(11) DEFAULT NULL,
  `LH` int(11) DEFAULT NULL,
  `PH` int(11) DEFAULT NULL,
  `TH` int(11) DEFAULT NULL,
  `CH` int(11) DEFAULT NULL,
  `Type` varchar(20) DEFAULT NULL,
  `Remark` varchar(50) DEFAULT NULL,
  `Origin` varchar(50) DEFAULT NULL,
  `Program` varchar(50) DEFAULT NULL,
  `year_of_study` int(11) DEFAULT NULL,
  `semester` varchar(20) DEFAULT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course_info`
--

INSERT INTO `course_info` (`CODE`, `COURSE_NAME`, `CU`, `LH`, `PH`, `TH`, `CH`, `Type`, `Remark`, `Origin`, `Program`, `year_of_study`, `semester`, `id`) VALUES
('BSE1106', 'Problem Solving and Programming Concepts', 4, 30, 30, 30, 60, 'Core', 'Modified', 'NW', 'BSSE', 1, 'Semester I', 1),
('UNV1101', 'Communication Skills', 4, 30, 60, 60, 0, 'Core', 'Old Language -', '', 'BSSE', 1, 'Semester I', 2),
('BSE1107', 'Mathematics for Software Engineers', 3, 30, 0, 30, 45, 'Core', 'New NW', '', 'BSSE', 1, 'Semester I', 3),
('BSE1108', 'Technical Analysis and Design', 4, 30, 30, 30, 60, 'Core', 'New NW', '', 'BSSE', 1, 'Semester I', 4),
('IST1101', 'Foundations of Information Systems & Technology', 4, 45, 30, 0, 60, 'Core', 'Old IS', '', 'BSSE', 1, 'Semester I', 5),
('CSC1109', 'Computer Literacy', 4, 30, 30, 30, 60, 'Audit Course', 'Old CS', '', 'BSSE', 1, 'Semester I', 6),
('BSE1206', 'Software Development Principles', 3, 45, 0, 0, 45, 'Core', 'Old NW', '', 'BSSE', 1, 'Semester II', 7),
('MTH2203', 'Numerical Analysis I', 3, 30, 0, 30, 45, 'Core', 'Old Math', '', 'BSSE', 1, 'Semester II', 8),
('BSE1209', 'Object-Oriented Programming I', 4, 30, 30, 30, 60, 'Core', 'New NW', '', 'BSSE', 1, 'Semester II', 9),
('IST1203', 'Data and Information Management I', 4, 30, 60, 0, 60, 'Core', 'Old IS', '', 'BSSE', 1, 'Semester II', 10),
('BSE1208', 'Introduction to Web Development', 4, 30, 30, 30, 60, 'Core', 'New NW', '', 'BSSE', 1, 'Semester II', 11),
('BSE1302', 'Software Engineering Practical Skills Project I', 5, 0, 150, 0, 75, 'Core', 'Old NW', '', 'BSSE', 1, 'Recess', 12),
('CSC2114', 'Artificial Intelligence', 4, 30, 30, 30, 60, 'Core', 'Modified CS', '', 'BSSE', 2, 'Semester I', 13),
('CSC2100', 'Data Structures and Algorithms', 4, 30, 30, 30, 60, 'Core', 'Old CS', '', 'BSSE', 2, 'Semester I', 14),
('BSE2106', 'Computer Networks', 4, 30, 30, 30, 60, 'Core', 'Old NW', '', 'BSSE', 2, 'Semester I', 15),
('BSE2105', 'Formal Methods', 3, 45, 0, 0, 45, 'Core', 'Old NW', '', 'BSSE', 2, 'Semester I', 16),
('BSE2107', 'Object-Oriented Programming II', 4, 30, 30, 30, 60, 'Core', 'New NW', '', 'BSSE', 2, 'Semester I', 17),
('CSC2200', 'Operating Systems', 4, 30, 30, 30, 60, 'Core', 'Modified CS', '', 'BSSE', 2, 'Semester II', 18),
('BSE2207', 'Emerging Web Development Technologies', 4, 30, 30, 30, 60, 'Core', 'New NW', '', 'BSSE', 2, 'Semester II', 19),
('BSE2208', 'Requirements Engineering', 3, 45, 0, 0, 45, 'Core', 'Modified NW', '', 'BSSE', 2, 'Semester II', 20),
('BSE2209', 'Mobile Programming Project', 4, 15, 60, 30, 60, 'Core', 'New NW', '', 'BSSE', 2, 'Semester II', 21),
('BSE2206', 'Data Communication', 4, 45, 30, 30, 60, 'Core', 'Old NW', '', 'BSSE', 2, 'Semester II', 22),
('BSE2302', 'Software Engineering Practical Skills Project II', 5, 0, 150, 0, 75, 'Core', 'Old NW', '', 'BSSE', 2, 'Recess', 23),
('BSE3110', 'Object-Oriented Analysis and Design', 4, 30, 30, 30, 60, 'Core', 'Old NW', '', 'BSSE', 3, 'Semester I', 24),
('BSE3111', 'Embedded Systems I', 4, 30, 30, 30, 60, 'Core', 'New NW', '', 'BSSE', 3, 'Semester I', 25),
('BSE3104', 'Software Metrics', 3, 45, 0, 0, 45, 'Core', 'Old NW', '', 'BSSE', 3, 'Semester I', 26),
('CSC3110', 'User Interface Design', 4, 30, 30, 30, 60, 'Core', 'Modified CS', '', 'BSSE', 3, 'Semester I', 27),
('BSE3106', 'Mobile Networks and Computing', 4, 45, 30, 0, 45, 'Elective', 'Old NW', '', 'BSSE', 3, 'Semester I', 28),
('BSE3105', 'Software Evolution', 4, 45, 0, 30, 60, 'Elective', 'Old NW', '', 'BSSE', 3, 'Semester I', 29),
('BSE3210', 'Software Architecture and Patterns', 3, 45, 0, 0, 45, 'Core', 'New NW', '', 'BSSE', 3, 'Semester II', 30),
('BSE3211', 'Software Testing and Verification', 3, 45, 0, 0, 45, 'Core', 'New NW', '', 'BSSE', 3, 'Semester II', 31),
('IST2203', 'Research Methodology', 4, 45, 0, 30, 60, 'Core', 'Old IT', '', 'BSSE', 3, 'Semester II', 32),
('CSC2206', 'Machine Learning ', 4, 0, 0, 0, 0, '', '', '', 'BSSE', 3, 'Semester II', 33),
('BSE3214', 'Cloud Computing and Big Data', 4, 30, 30, 30, 60, 'Elective', 'New NW', '', 'BSSE', 3, 'Semester II', 34),
('BSE3213', 'Embedded Systems II', 4, 30, 30, 30, 60, 'Elective', 'New NW', '', 'BSSE', 3, 'Semester II', 35),
('BSE3302', 'Field Attachment', 5, 0, 150, 0, 75, 'Core', 'Old NW', '', 'BSSE', 3, 'Recess', 36),
('BSE4100', 'Software Engineering Project I', 5, 0, 150, 0, 75, 'Core', 'Old NW', '', 'BSSE', 4, 'Semester I', 37),
('BSE4102', 'ICT Innovation and Entrepreneurship', 3, 45, 0, 0, 45, 'Core', 'New NW', '', 'BSSE', 4, 'Semester I', 38),
('BSE4104', 'Emerging Trends in Software Engineering', 3, 45, 0, 0, 45, 'Core', 'Modified NW', '', 'BSSE', 4, 'Semester I', 39),
('BSE4105', 'Software Integration and Deployment', 4, 30, 60, 0, 60, 'Core', 'New NW', '', 'BSSE', 4, 'Semester I', 40),
('BSE4200', 'Software Engineering Project II', 5, 0, 150, 0, 75, 'Core', 'Old NW', '', 'BSSE', 4, 'Semester II', 41),
('BSE4202', 'Software Security', 4, 30, 60, 0, 60, 'Core', 'Modified NW', '', 'BSSE', 4, 'Semester II', 42),
('BSE4203', 'Software Engineering Standards and Ethics', 3, 45, 0, 0, 45, 'Core', 'New NW', '', 'BSSE', 4, 'Semester II', 43),
('BSE4204', 'Software Quality Management', 3, 45, 0, 0, 45, 'Core', 'New NW', '', 'BSSE', 4, 'Semester II', 44);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-08-06 11:00:53.976425'),
(2, 'auth', '0001_initial', '2023-08-06 11:00:54.840023'),
(3, 'admin', '0001_initial', '2023-08-06 11:00:55.019192'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-08-06 11:00:55.035704'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-08-06 11:00:55.055184'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-08-06 11:00:55.199707'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-08-06 11:00:55.311013'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-08-06 11:00:55.365233'),
(9, 'auth', '0004_alter_user_username_opts', '2023-08-06 11:00:55.384759'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-08-06 11:00:55.502715'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-08-06 11:00:55.510749'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-08-06 11:00:55.529664'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-08-06 11:00:55.581925'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-08-06 11:00:55.643175'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-08-06 11:00:55.692373'),
(16, 'auth', '0011_update_proxy_permissions', '2023-08-06 11:00:55.715406'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-08-06 11:00:55.761200'),
(18, 'feedback', '0001_initial', '2023-08-06 11:00:55.796627');

-- --------------------------------------------------------

--
-- Table structure for table `feedback_course`
--

CREATE TABLE `feedback_course` (
  `id` bigint(20) NOT NULL,
  `COURSE_NAME` varchar(255) DEFAULT NULL,
  `year_of_study` int(11) DEFAULT NULL,
  `semester` varchar(50) DEFAULT NULL,
  `CU` int(11) DEFAULT NULL,
  `LH` int(11) DEFAULT NULL,
  `Origin` varchar(50) DEFAULT NULL,
  `PH` int(11) DEFAULT NULL,
  `Remark` varchar(50) DEFAULT NULL,
  `TH` int(11) DEFAULT NULL,
  `Type` varchar(50) DEFAULT NULL,
  `program` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `student_answers`
--

CREATE TABLE `student_answers` (
  `lecturer_preparedness` varchar(255) DEFAULT NULL,
  `lecturer_interest` varchar(255) DEFAULT NULL,
  `feedback_useful` varchar(255) DEFAULT NULL,
  `lecturers_complement` text DEFAULT NULL,
  `instructional_materials` varchar(255) DEFAULT NULL,
  `course_organization` varchar(255) DEFAULT NULL,
  `confidence_in_advanced_work` varchar(255) DEFAULT NULL,
  `exam_measurement` varchar(255) DEFAULT NULL,
  `concept_understanding` varchar(255) DEFAULT NULL,
  `concept_understanding_feedback` varchar(255) DEFAULT NULL,
  `applicability` varchar(255) DEFAULT NULL,
  `applicability_reasoning` text DEFAULT NULL,
  `recommend_course` varchar(255) DEFAULT NULL,
  `card_info_id` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_answers`
--

INSERT INTO `student_answers` (`lecturer_preparedness`, `lecturer_interest`, `feedback_useful`, `lecturers_complement`, `instructional_materials`, `course_organization`, `confidence_in_advanced_work`, `exam_measurement`, `concept_understanding`, `concept_understanding_feedback`, `applicability`, `applicability_reasoning`, `recommend_course`, `card_info_id`) VALUES
('almost_always', 'almost_always', 'rarely', 'almost_always', 'rarely', 'agree', 'neutral', 'strongly_disagree', '1', 'nsksdv', '2', 'kz kz', '0', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `course_info`
--
ALTER TABLE `course_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedback_course`
--
ALTER TABLE `feedback_course`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `course_info`
--
ALTER TABLE `course_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `feedback_course`
--
ALTER TABLE `feedback_course`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
