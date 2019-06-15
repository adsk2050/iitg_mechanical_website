-- phpMyAdmin SQL Dump
-- version 3.5.8
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 12, 2019 at 06:09 PM
-- Server version: 5.1.61
-- PHP Version: 5.3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `mechdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_staff`
--

CREATE TABLE IF NOT EXISTS `tbl_staff` (
  `Email` varchar(64) NOT NULL,
  `First_Name` varchar(64) NOT NULL,
  `Middle_Name` varchar(64) NOT NULL,
  `Last_Name` varchar(64) NOT NULL,
  `Designation` varchar(255) NOT NULL,
  `Associated_Lab` varchar(255) DEFAULT NULL,
  `Phone` int(7) unsigned DEFAULT NULL,
  `Password` char(128) NOT NULL,
  `Photo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_staff`
--

INSERT INTO `tbl_staff` (`Email`, `First_Name`, `Middle_Name`, `Last_Name`, `Designation`, `Associated_Lab`, `Phone`, `Password`, `Photo`) VALUES
('jitenb', 'Jiten ', '', 'Basumatary', 'Technical Superintendent ', 'Advanced Manufacturing, Metrology, Thermal Science, Fluid Mechanics', 2582690, '', NULL),
('nip', 'Nip ', '', 'Borah', 'Technical Superintendent ', 'Computer Aided Design, Mechatronics and Turbo Machinery', 2583446, '', NULL),
('sanjib.s', 'Sanjib ', '', 'Sarma', 'Technical Superintendent', 'Strength of Materials and Theory of Machines', 2582689, '', NULL),
('bijoy.k', 'Bijoy', 'Kr. ', 'Choudhury', 'Jr. Technical Superintendent', 'Machine Shop (Lathe)', 2582698, '', NULL),
('dhani', 'Dhaneswar ', '', 'Khaklary', 'Jr. Technical Superintendent', 'Machine Shop (Lathe)', 2582698, '', NULL),
('chetri', 'Dilip ', '', 'Chetri', 'Technical Superintendent', 'Welding Shop', 2582698, '', NULL),
('dkd', 'Dipak ', 'Kr. ', 'Deka', 'Jr. Technical Superintendent', 'Machine Shop', 2582698, '', NULL),
('joykrishna', 'Joykrishna', '', 'Saikia', 'Jr. Technical Superintendent', 'IC Engine & EDM Machine', 2582698, '', NULL),
('lng', 'Lakhinath ', '', 'Gogoi', 'Jr. Technical Superintendent', 'Carpentry Shop', 2582698, '', NULL),
('minesh', 'Minesh ', 'Ch. ', 'Medhi', 'Technical Superintendent', 'Machine Shop (Milling)', 2582698, '', NULL),
('mrinal_s', 'Mrinal ', '', 'Sarma', 'Technical Superintendent', 'Fitting Shop', 2582698, '', NULL),
('m.baishya', 'Monoj ', 'Kr. ', 'Baishya', 'Technical Superintendent', 'CNC Lab and Sheet Metal', 2582698, '', NULL),
('nidul_s', 'Nidul ', '', 'Saikia', 'Jr. Technical Superintendent', 'Machine Shop (Milling)', 2582698, '', NULL),
('ug', 'Upen ', '', 'Gohain', 'Jr. Technical Superintendent', 'Machine Shop (Lathe)', 2582698, '', NULL),
('banikya.chandan', 'Chandan ', '', 'Banikya', 'Technical Superintendent', 'Workshop and I. C. Engine', 2583443, '', NULL),
('monudh', 'Monuranjan ', '', 'Dowarah', 'Technical Superintendent', 'Fluid Mechanics, Instrumentation and Control, Mechatronics and Robotics', 2582688, '', NULL),
('saifuddin', 'Saiffuddin ', '', 'Ahmed', 'Technical Superintendent', 'Material Science, Turbo-Machinary', 2582694, '', NULL),
('naba', 'Nabajyoti ', '', 'Dutta', 'Jr. Superintendent', 'Department Office', 2582700, '', NULL),
('raju.talukdar', 'Raju', '', 'Talukdar', 'Jr. Assistant', 'Department Office', 2582700, '', NULL),
('porag_s', 'Porag', '', 'Saikia', 'Jr. Technical Superintendent', 'CNC lab, Workshop', 2582698, '', NULL),
('dulumonidas', 'Dulumoni ', '', 'Das', 'Jr. Technician ', 'Workshop', 2582698, '', NULL),
('ganesh81', 'Ganesh', '', 'Nath ', 'Jr. Technician', 'Workshop', 2582698, '', NULL),
('medhir58', 'Ratan ', '', 'Medhi', 'Jr. Technician', 'Workshop', 2582698, '', NULL),
('gakul84', 'Gakul', '', 'Das', 'Jr. Technician', 'Workshop', 2582698, '', NULL),
('santoshgogoi', 'Santush', '', 'Gogoi', 'Jr. Technician', 'Workshop', 2582698, '', NULL),
('gautamgogoi', 'Gautam', '', 'Gogoi', 'Jr. Technician', 'Workshop', 2582698, '', NULL),
('gwms90', 'Gwmchar ', '', 'Baro', 'Jr. Technician', 'Workshop', 2583443, '', NULL);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
