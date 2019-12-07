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
-- Table structure for table `tbl_officers`
--

CREATE TABLE IF NOT EXISTS `tbl_officers` (
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
-- Dumping data for table `tbl_officers`
--

INSERT INTO `tbl_officers` (`Email`, `First_Name`, `Middle_Name`, `Last_Name`, `Designation`, `Associated_Lab`, `Phone`, `Password`, `Photo`) VALUES
('pranjol', 'Pranjol', '', 'Paul', 'Technical Officer Gr I', 'Advanced Manufacturing, Computer Aided Design, Tribology and Theory of Machines', 2582683, '', NULL),
('rsaikia', 'Rituraj', '', 'Saikia', 'Technical Officer Gr I', 'Material Science, Strength of Materials, Thermal Science and Turbo Machinery', 2582682, '', NULL),
('amal', 'Amal', '', 'Kalita', 'Junior Technical Officer ', 'Computer Aided Design', 2582695, '', NULL),
('djb', 'Dhruba', 'Jyoti', 'Bordoloi', 'Technical Officer Gr II  ', 'Vibration and Acoustics, Mechatronics and Robotics, Instrumentation and Control  ', 2583432, '', NULL),
('j.kakati', 'Jyotirmoy', '', 'Kakati ', 'Technical Officer Gr II', 'Fluid Mechanics, IC Engine, Wind Tunnel and 3D Printing ', 2583442, '', NULL),
('nandan', 'Nandan', 'Kanan', 'Das', 'Asst. Workshop Superintendent', 'Workshop and Advanced Manufacturing Laboratory', 2583414, '', NULL);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
