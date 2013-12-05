-- phpMyAdmin SQL Dump

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `rkfake`
--

-- --------------------------------------------------------

--
-- Table structure for table `infohash`
--

CREATE TABLE IF NOT EXISTS `infohash` (
  `id` int(11) NOT NULL auto_increment,
  `announce_server` text NOT NULL,
  `info_hash` text NOT NULL,
  `peer_id` text NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

