-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 12, 2025 at 07:45 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `cyberiot1`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `uname` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--


-- --------------------------------------------------------

--
-- Table structure for table `datablock`
--

CREATE TABLE `datablock` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `maddress` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `b1` varchar(1000) NOT NULL,
  `b2` varchar(1000) NOT NULL,
  `status` varchar(50) NOT NULL,
  `date` varchar(10) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `datablock`
--

INSERT INTO `datablock` (`id`, `name`, `maddress`, `fname`, `b1`, `b2`, `status`, `date`) VALUES
(1, 'mani', 'A0-36-BC-26-CD-ED', 'Try To Access Machine Controls', '0', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '', '2025-04-02'),
(2, 'mani', 'A0-36-BC-26-CD-ED', 'Try To Access Data Controls', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '', '2025-04-02'),
(3, 'mani', 'A0-36-BC-26-CD-ED', 'Try To Access Data Controls', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '', '2025-04-02'),
(4, 'mani', 'A0-36-BC-26-CD-ED', 'Try To Access Machine Controls', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '', '2025-04-02'),
(5, 'mani', 'A0-36-BC-26-CD-ED', 'Try To Access Machine Controls', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '', '2025-04-02'),
(6, 'mani', 'A0-36-BC-26-CD-ED', 'Try To Access Data Controls', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '', '2025-04-02'),
(7, 'mani', 'A0-36-BC-26-CD-ED', 'Try To Access Machine Controls', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '', '2025-04-02'),
(8, 'mani', 'A0-36-BC-26-CD-ED', 'Try To Access Machine Controls', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '', '2025-05-12'),
(9, 'mani', 'A0-36-BC-26-CD-ED', 'Try To Access Machine Controls', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '', '2025-05-12'),
(10, 'mani', 'A0-36-BC-26-CD-ED', 'Try To Access Machine Controls', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '', '2025-05-13'),
(11, 'mani', 'A0-36-BC-26-CD-ED', 'Try To Access Machine Controls', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '', '2025-05-13'),
(12, 'mani', 'A0-36-BC-26-CD-ED', 'Try To Access Machine Controls', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '3d1f7e54ba8585ebf7a0906edc6440b577f4b371', '', '2025-05-13');

-- --------------------------------------------------------

--
-- Table structure for table `iotdata`
--

CREATE TABLE `iotdata` (
  `id` int(50) NOT NULL auto_increment,
  `date` varchar(100) NOT NULL,
  `load_temperature` varchar(100) NOT NULL,
  `envi_humidity` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `iotdata`
--

INSERT INTO `iotdata` (`id`, `date`, `load_temperature`, `envi_humidity`, `status`) VALUES
(1, '2025-05-13', 'qaZFqZxGMpbK16BCGUlFVQ==', '6OYMiMjH3arvXok4Lvbh9A==', '0');

-- --------------------------------------------------------

--
-- Table structure for table `iotdata1`
--

CREATE TABLE `iotdata1` (
  `id` int(50) NOT NULL auto_increment,
  `date` varchar(100) NOT NULL,
  `load_temperature` varchar(100) NOT NULL,
  `envi_humidity` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `iotdata1`
--

INSERT INTO `iotdata1` (`id`, `date`, `load_temperature`, `envi_humidity`, `status`) VALUES
(1, '2025-05-13', 'yNSeQIWQfCk0wjgLhSy/qg==', 'ZElIWhZDLiu02MTfLfO02A==', '0');

-- --------------------------------------------------------

--
-- Table structure for table `newdata`
--

CREATE TABLE `newdata` (
  `id` int(50) NOT NULL auto_increment,
  `sno` varchar(50) NOT NULL,
  `file` varchar(50) NOT NULL,
  `details` varchar(100) NOT NULL,
  `b0` varchar(1000) NOT NULL,
  `b1` varchar(1000) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `newdata`
--

INSERT INTO `newdata` (`id`, `sno`, `file`, `details`, `b0`, `b1`) VALUES
(1, '1', 'main.py', 'test', '0', '184b37337a27eb134f2fe3a936a7e0c92be53490');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `maddress` varchar(100) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `acontrol` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `phone`, `email`, `maddress`, `uname`, `password`, `acontrol`) VALUES
(1, 'mani', '8890334522', 'sundarv06@gmail.com', 'A0-36-BC-26-CD-EJ', 'mani', 'mani', '1'),
(2, 'sundar', '7904461600', 'sundarv06@gmail.com', 'A0-36-BC-26-CD-ED', 'admin', 'admin', 'Full Access 1'),
(3, 'mani', '8890334522', 'yogisamcore5@gmail.com', 'A0-36-BC-26-CD-ED', 'a123', 'a123', 'Full Access 2');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(255) default NULL,
  `email` text,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`) VALUES
(1, 'john_doe', 'a05voLnPp+ufeoz6p2bPCoHo7BlbTNJEt5/feY6i7PM=');
