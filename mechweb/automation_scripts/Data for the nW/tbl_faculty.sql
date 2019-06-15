-- phpMyAdmin SQL Dump
-- version 3.5.8
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 14, 2019 at 05:33 PM
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
-- Table structure for table `tbl_faculty`
--

CREATE TABLE IF NOT EXISTS `tbl_faculty` (
  `Email` varchar(64) NOT NULL,
  `First_Name` varchar(64) NOT NULL,
  `Middle_Name` varchar(64) NOT NULL,
  `Last_Name` varchar(64) NOT NULL,
  `Designation` varchar(255) NOT NULL,
  `Group` varchar(255) NOT NULL,
  `Research_Interests` varchar(300) DEFAULT NULL,
  `Phone` int(7) unsigned DEFAULT NULL,
  `Office` char(15) DEFAULT NULL,
  `Alma_Mater` varchar(255) DEFAULT NULL,
  `Password` char(128) NOT NULL,
  `Webpage` varchar(255) DEFAULT NULL,
  `abbr` text NOT NULL,
  `Joining` int(7) NOT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_faculty`
--

INSERT INTO `tbl_faculty` (`Email`, `First_Name`, `Middle_Name`, `Last_Name`, `Designation`, `Group`, `Research_Interests`, `Phone`, `Office`, `Alma_Mater`, `Password`, `Webpage`, `abbr`, `Joining`) VALUES
('amaresh', 'Amaresh', '', 'Dalal', 'Associate Professor', 'Fluids and Thermal Engineering', 'Computational Fluid Dynamics, Heat Transfer,  Structured Grid Techniques in Curvilinear Coordinates, Finite Volume Methods and Unstructured Grid Techniques, Natural and Mixed Convection Flows, Electrochemical Energy Conversion and Storage', 2582677, 'C-106', 'IIT Kanpur', '', 'http://www.iitg.ac.in/amaresh', 'AMD', 2010),
('anoop', 'Anoop', 'K.', 'Dass', 'Professor', 'Fluids and Thermal Engineering', 'Computational Fluid Dynamics and Turbomachines', 2582654, 'C-205', 'IISc Bangalore', '', 'http://www.iitg.ac.in/anoop', 'AD', 1996),
('akd', 'Arnab', 'Kumar', 'De', 'Associate Professor', 'Fluids and Thermal Engineering', 'Numerical Methods in Fluid Flow and Heat Transfer, Convection, Turbulence', 2582672, 'C-302', 'IIT Kanpur', '', 'http://www.iitg.ac.in/akd', 'AKD', 2009),
(' bsandeepr', 'Sandeep', 'Reddy', 'Basireddy', 'Assistant Professor', 'Machine Design', 'Nonlinear Dynamics of Mechanical Systems, Robotics and Control, Applied Dynamics', NULL, 'D-304', 'IISC Bangalore', '', 'http://www.iitg.ac.in/ bsandeepr', '', 2018),
('dnbasu', 'Dipankar', 'Narayan', 'Basu', 'Associate Professor', 'Fluids and Thermal Engineering', 'Nuclear Thermalhydraulics, Supercritical Natural Circulation Loops, Domestic Air-conditioning, Computational Fluid Dynamics and Heat Transfer', 2583431, 'C-203', 'IIT Kharagpur', '', 'http://www.iitg.ac.in/dnbasu', 'DNB', 2012),
('n.ganesh', 'Ganesh', '', 'Natarajan', 'Associate Professor (on deputation)', 'Fluids and Thermal Engineering', 'Computational Fluid dynamics, Grid Adaptation, Error Estimation, Immersed Boundary methods, Parallel computing, Biofluid dynamics', 2582685, 'D-308', 'IISc Bangalore', '', 'https://sites.google.com/site/ganucfd', 'GN', 2011),
('gmadhu', 'Gavara', '', 'Madhusudhana', 'Assistant Professor', 'Fluids and Thermal Engineering', 'Computational Fluid Dynamics, Heat Transfer, Cooling of Electronics, Multi-phase flows, Cooling at Micro/Mini scales, Turbulent Fluid Flow and Heat transfer', 2583429, 'D-102', 'IISc Bangalore', '', 'http://www.iitg.ac.in/gmadhu', 'GM', 2012),
('manmohan', 'Manmohan', '', 'Pandey', 'Professor', 'Fluids and Thermal Engineering', 'Dynamics and Control of Fluid-Thermal Systems, Nuclear Reactor Thermal-Hydraulics', 2582687, 'FR-2, ME Extn.', 'IIT Kanpur', '', 'http://www.iitg.ernet.in/engfac/manmohan/public_html/index.htm', 'MP', 2000),
('shock', 'Niranjan', '', 'Sahoo', 'Professor', 'Fluids and Thermal Engineering', 'Fluid and Thermal Engineering, Aerodynamics, Gas Dynamics, Instrumentation, Measurements and Experiments in Fluid', 2582665, 'C-202', 'IISc Bangalore', '', 'http://www.iitg.ac.in/mech/files/faculty_CV/Website-CV-NS.pdf', 'NS', 2004),
('pinak', 'Pinakeswar', '', 'Mahanta', 'Professor (on deputation)', 'Fluids and Thermal Engineering', 'Thermal Radiation with Participating Media, Fluidization, Energy Conservation and Renewable Energy', 2582662, 'C-208', 'IIT Guwahati', '', 'http://www.iitg.ac.in/mech/files/faculty_CV/PM-CV-2013.pdf', 'PM', 2001),
('pmkumar', 'P.', '', 'Muthukumar', 'Professor', 'Fluids and Thermal Engineering', 'Coupled heat and mass transfer analysis; Metal hydride based thermal machines, Conventional and Non-conventional refrigeration systems', 2582673, 'C-303', 'IIT Madras', '', 'http://www.iitg.ernet.in/pmkumar/', 'PMK', 2006),
('arupn', 'Arup', '', 'Nandy', 'Assistant Professor', 'Machine Design Engineering', 'Finite Element Development and Analysis in Structure, Acoustics, Electromagnetics, Structural acoustic interaction, Magnetohydrodynamics, MEMS;  Optimization', 2583441, 'C-307', NULL, '', 'http://www.iitg.ac.in/arupn', '', 2017),
('saha', 'Ujjwal', 'K.', 'Saha', 'Professor', 'Fluids and Thermal Engineering', 'Propulsion, Turbomachinery, Wind Energy Conversion, Internal Combustion Engines', 2582663, 'C-107', 'IIT Bombay', '', 'http://www.iitg.ac.in/mech/files/faculty_CV/me-fac-uksaha.pdf', 'UKS', 2000),
('vinayak', 'Vinayak', '', 'Kulkarni', 'Associate Professor', 'Fluids and Thermal Engineering', 'High enthalpy flows, scramjet engine, experimental, aerodynamics, measurement science, CFD simulations', 2582655, 'C-204', 'IISc Bangalore', '', 'https://sites.google.com/site/kulksaero/', 'VK', 2008),
('ads', 'Anil', 'D.', 'Sahasrabudhe', 'Professor (on deputation)', 'Machine Design Engineering', 'Vibration and Noise, Condition Monitoring, CAD/CAM', NULL, NULL, 'IISc Bangalore', '', 'http://www.iitg.ac.in/mech/faculty/ads.htm', 'ADS', 1995),
('atanub', 'Atanu', '', 'Banerjee', 'Associate Professor', 'Machine Design Engineering', 'Complaint Mechanism, Shape memory alloy, Bio-memetic devices', 2582679, 'FR-21, ME Extn.', 'IIT Kanpur', '', 'https://sites.google.com/site/dratanubanerjee', 'AB', 2010),
('chakra', 'Debabrata', '', 'Chakraborty', 'Professor', 'Machine Design Engineering', 'FRP, Composites, FEM, Fracture Mechanics and Design', 2582666, 'D-306', 'IIT Kharagpur', '', 'http://www.iitg.ernet.in/engfac/chakra/public_html/', 'DC', 1999),
('dsharma', 'Deepak', '', 'Sharma', 'Associate Professor', 'Machine Design Engineering', 'Multi-objective Optimization, Structural Topology Optimization, and Combinatorial Optimization using Evolutionary Algorithms', 2582661, 'C-104', 'IIT Kanpur', '', 'http://www.iitg.ac.in/dsharma', 'DS', 2012),
('dibakarb', 'Dibakar', '', 'Bandopadhya', 'Associate Professor', 'Machine Design Engineering', 'Active materials, Artificial muscle materials, Smart structures, Robotics and mechanism, Composites, MEMS, Bio inspired design\n', 2582653, 'D-208', 'IIT Kanpur', '', 'http://www.iitg.ac.in/dibakarb', 'DB', 2008),
('ksrkm', 'K. S. R.', 'Krishna', 'Murthy', 'Professor', 'Machine Design Engineering', 'Finite Element Methods, Error Estimation and Fracture Mechanics', 2582658, 'D-204', 'IIT Kharagpur', '', 'http://www.iitg.ac.in/ksrkm', 'KSRKM', 2002),
('karuna.kalita', 'Karuna', '', 'Kalita', 'Associate Professor', 'Machine Design Engineering', 'Rotordynamics, Coupled Dynamics of Electro-Mechanical Systems, Vibration', 2582680, 'D-302', 'University of Nottingham', '', 'http://www.iitg.ac.in/karuna.kalita', 'KK', 2010),
('kpmech', 'Poonam', '', 'Kumari', 'Associate Professor', 'Machine Design Engineering', 'Theory of plates and shells, Computational mechanics, Smart structures', 2583434, 'D-201', 'IIT Delhi', '', 'http://www.iitg.ac.in/kpmech', 'PK', 2013),
('rtiwari', 'Rajiv', '', 'Tiwari', 'Professor', 'Machine Design Engineering', 'Rotor Dynamics, Vibrations, Identification in Mechanical Systems, Rolling Element Bearing Design and Analysis, Application of Active Magnetic Bearings in Rotors, Vibrations based Condition Monitoring of Industrial Rotating Machines', 2582667, 'C-206', 'IIT Kanpur', '', 'http://www.iitg.ernet.in/engfac/rtiwari/resume/index.html', 'RT', 1997),
('ssg', 'Sachin', 'S.', 'Gautam', 'Assistant Professor', 'Machine Design Engineering', 'Design and Manufacturing : Nonlinear Finite Element Analysis, Computational Contact Impact Analysis, Adhesion, Rough Surfaces, Time Integration Schemes, Mixed Time Integration Schemes, Plasticity, Ductile Fracture, Continuum Damage Mechanics', 2583433, 'D-103', 'IIT Kanpur', '', 'http://www.iitg.ac.in/ssg', 'SSG', 2013),
('sangu', 'Sangamesh', 'Deepak', 'R', 'Assistant Professor (on lien)', 'Machine Design Engineering', 'Kinematics and Dynamics of rigid multi-body systems, Compliant Mechanisms, Topology Optimization, Static Balancing', 2583432, 'D-307', 'IISc Bangalore', '', 'http://www.iitg.ac.in/sangu', 'SDR', 2013),
('dwivedy', 'Santosha', 'K.', 'Dwivedy', 'Professor & HOD', 'Machine Design Engineering', 'Non-linear Dynamics, Design and Robotics, vibrations', 2582670, 'C-207', 'IIT Kharagpur', '', 'http://www.iitg.ernet.in/engfac/dwivedy/public_html/index.html', 'SKD', 1999),
('sashin', 'Sashindra', 'K.', 'Kakoty', 'Professor', 'Machine Design Engineering', 'Tribology, Duct Acoustics, Mechanical System Design, Rural Technology', 2582659, 'C-103', 'IIT Kharagpur', '', 'http://www.iitg.ac.in/mech/files/faculty_CV/SKK_profile.pdf', 'SKK', 2000),
('spanda', 'Satyajit', '', 'Panda', 'Associate Professor', 'Machine Design Engineering', 'Composite materials, Nonlinear vibrations, Smart materials and structures, FEM, Functionally Graded materials and structures, Micromechanics.', 2582664, 'C-304', 'IIT Kharagpur', '', 'http://www.iitg.ac.in/spanda/spanda.pdf', 'SP', 2009),
('kanagaraj', 'S.', '', 'Kanagaraj', 'Professor', 'Machine Design Engineering', 'Biomaterials, Carbon nanotubes based nanocomposites, Nanofluids, Materials characterization', 2582676, 'D-305', 'IIT Kharagpur', '', 'http://www.iitg.ac.in/kanagaraj', 'SK', 2008),
('ssvelan', 'S.', '', 'Senthilvelan', 'Professor', 'Machine Design Engineering', 'Composites, Fatigue, Wear and Failure Analysis', 2582671, 'C-306', 'IIT Madras', '', 'http://www.iitg.ernet.in/engfac/ssvelan/public_html/index.html\n', 'SSV', 2006),
('uday', 'Uday', 'S.', 'Dixit', 'Professor', 'Machine Design and manufacturing Engineering', 'Design and Manufacturing : FEM, Neural Network and Fuzzy Set Application; Mechatronics', 2582657, 'D-206', 'IIT Kanpur', '', 'http://www.iitg.ac.in/uday', 'USD', 1998),
('manasdas', 'Manas', '', 'Das', 'Associate Professor', 'Manufacturing Engineering', 'Advanced Finishing and Nano-finishing Processes, Non-traditional Machining Processes, Machining of Advanced Engineering Materials, Micromanufacturing, Micromachining, Tribology, Laser Welding', 2583427, 'C-108', 'IIT Kanpur', '', 'http://www.iitg.ac.in/manasdas', 'MD', 2012),
('evmrs', 'Ravi', 'M.', 'Sankar', 'Assistant Professor (on deputation)', 'Manufacturing Engineering', 'Machining & Advanced Machining Processes, MEMS & NEMS, Sustainable Machining, Micromanufacturing, Composite Materials, Online monitoring of Manufacturing Processes, Tribology, Precision Engineering', 2582684, 'C-308', 'IIT Kanpur', '', 'http://www.iitg.ac.in/evmrs', 'MRS', 2012),
('pankaj.biswas', 'Pankaj', '', 'Biswas', 'Associate Professor', 'Manufacturing Engineering', 'Manufacturing and Design: Computational weld mechanics, Solid state welding, Soft computing modeling of welding processes, FEM, Line heating', 2582675, 'D-207', 'IIT Kharagpur', '', 'http://www.iitg.ac.in/pankaj.biswas', 'PB', 2011),
('psr', 'P.', 'S.', 'Robi', 'Professor', 'Manufacturing Engineering', 'Coating, Fracture Mechanics, Materials Processing, Metal Matrix composite, Metal Casting, P/M Processing', 2582668, 'D-205', 'IIT Bombay', '', 'http://www.iitg.ac.in/psr/', 'PSR', 1997),
('ganu', 'Ganesh', 'R.', 'Narayanan', 'Associate Professor', 'Manufacturing Engineering', 'Material Forming and Joining', 2582669, 'D-301', 'IIT Bombay', '', 'http://www.iitg.ernet.in/engfac/ganu/public_html/index.html', 'RGN', 2007),
('sdk', 'Sachin', 'D.', 'Kore', 'Associate Professor (on lien)', 'Manufacturing Engineering', 'Experimental and numerical study of electromagnetic pulse processing, Solid state welding, Joining of similar, dissimilar and lightweight metals like Al, Steel, Al-Li, and Mg', 2582652, 'D-304', 'IIT Bombay', '', 'http://www.iitg.ac.in/sdk', 'SDK', 2009),
('snj', 'Shrikrishna', 'N.', 'Joshi', 'Associate Professor', 'Manufacturing Engineering', 'Micro fabrication: Laser micro forming, Micro machining: Micro electric discharge machining (EDM), Web based manufacturing, Process modeling and optimization of advanced manufacturing processes, Application of soft computing techniques in manufacturing', 2582678, 'D-203', 'IIT Bombay', '', 'http://www.iitg.ac.in/snj', 'SNJ', 2010),
('spal', 'Sukhomay', '', 'Pal', 'Associate Professor', 'Manufacturing Engineering', 'Welding Process Monitoring and Control, Tool Condition Monitoring, Non-Conventional Machining Process Application of Artificial Neural Network, Genetic Algorithms and Fuzzy logic in manufacturing', 2582656, 'C-305', 'IIT Kharagpur', '', 'http://www.iitg.ac.in/spal', 'SUP', 2010),
('swarupbag', 'Swarup', '', 'Bag', 'Associate Professor', 'Manufacturing Engineering', 'Fusion welding processes, Finite element method, Laser microjoining, Heat transfer and fluid flow in fusion welding, Residual stress and distortion, Recrystallization in hot metal forming process, Optimization in manufacturing process', 2582686, 'C-102', 'IIT Bombay', '', 'https://sites.google.com/site/sbagiitg', 'SB', 2011),
('gtm', 'Gautam', '', 'Biswas', 'J C Bose National Fellow and Director of the Institute; Professor of ME', 'Fluids and Thermal Engineering', 'Computational Fluid Dynamics, Convective Heat Transfer, Turbulence, Boiling Heat Transfer, Heat Transfer Augmentation, Turbomachinery', 2582005, 'C-203', 'IIT Kharagpur', '', 'http://www.iitg.ernet.in/director/index.html', 'GTM', 2013),
('bhaskark', 'Bhaskar  ', '', 'Kumar', 'Assistant Professor', 'Fluids and Thermal Engineering', 'Hydrodynamic Stability, Bluff Body Flows, Computational Fluid Dynamics', 2583436, 'C-105', 'IIT Kanpur', '', 'www.iitg.ac.in/bhaskark', '', 2015),
('pranabm', 'Pranab', 'Kumar', 'Mondal', 'Assistant Professor', 'Fluids and Thermal Engineering', 'Microfluidics, Electrokinetics, Two Phase Transport, Microscale Transport of Heat, Flow Through Porous Media.', 2583435, 'C-101', 'IIT Kharagapur', '', 'http://www.iitg.ernet.in/pranabm', '', 2015),
('krishnab', 'Balkrishna', '', 'Mehta', 'Assistant Professor', 'Fluids and Thermal Engineering', 'Experimental investigation of heat transfer in two-phase flow in mini/micro systems, Heat pipes, Thermosyphons, Heat transfer investigation of ferrofluids in presence of magnetic field, InfraRed thermography for temperature measurements.', 2583439, 'FR-1, ME Extn.', 'IIT Kanpur', '', 'https://sites.google.com/site/krishnabiitg/', '', 2015),
('pkhanikar', 'Prasenjit ', '', 'Khanikar', 'Assistant Professor', 'Machine Design Engineering', 'Microstructural Materials Modeling, Micro-mechanics, Dislocation Density Based Crystal Plasticity, Deformation and Failure Mechanisms of Metallic Materials, Finite Element Method, Dynamic Behavior of Materials, Fracture Mechanics, Aluminum Alloys, Microstructural Characterization', 2583438, 'C-301', NULL, '', 'http://www.iitg.ac.in/pkhanikar', '', 2015),
('sajan.kapil', 'Sajan', '', 'Kapil', 'Assistant Professor', 'Machine Design and Manufacturing Engineering', 'Rapid Manufacturing (3D Printing),  Welding/Cladding Processes, CNC, Manufacturing  Automation', 2582652, 'FR-1, ME Extn.', 'IIT Bombay', '', 'http://www.iitg.ac.in/sajan.kapil', '', 2018),
('s.m.hazarika', 'Shyamanta', 'M.', 'Hazarika', 'Professor', 'Machine Design Engineering', 'Robotics, Cognitive Systems, Knowledge Representation and Reasoning', 2583437, 'FR-3, ME Extn.', NULL, '', 'http://www.iitg.ac.in/s.m.hazarika/', '', 2017),
('nelsonm', 'Nelson', '', 'Muthu', 'Assistant Professor', 'Machine Design Engineering', 'Meshfree Methods, FEM, Fracture Mechanics, Composites, Structural Health Monitoring, Medical Device Innovation', 2583440, 'C-201', 'IIT Bombay and Monash University', '', 'http://www.iitg.ac.in/nelsonm', '', 2017);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
