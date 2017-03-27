-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 2017-03-10 05:44:53
-- 服务器版本： 5.5.53-log
-- PHP Version: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `yzy_data`
--

-- --------------------------------------------------------

--
-- 表的结构 `yzy_class`
--

CREATE TABLE `yzy_class` (
  `id` int(11) NOT NULL,
  `cname` varchar(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `yzy_class`
--

INSERT INTO `yzy_class` (`id`, `cname`) VALUES
(1, '其它'),
(2, '音乐'),
(3, '图片'),
(4, '电子书'),
(5, '文档'),
(6, '种子'),
(7, '手机APP'),
(8, '影视'),
(9, '无损音乐'),
(10, '教程');

-- --------------------------------------------------------

--
-- 表的结构 `yzy_resources`
--

CREATE TABLE `yzy_resources` (
  `id` int(11) NOT NULL,
  `tid` tinyint(3) UNSIGNED NOT NULL,
  `cid` tinyint(3) UNSIGNED NOT NULL,
  `uid` int(11) NOT NULL,
  `title` varchar(80) NOT NULL,
  `size` varchar(10) NOT NULL,
  `url` varchar(255) NOT NULL,
  `pwd` varchar(10) NOT NULL,
  `description` varchar(100) NOT NULL,
  `available` tinyint(1) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `yzy_type`
--

CREATE TABLE `yzy_type` (
  `id` int(11) NOT NULL,
  `name` char(10) NOT NULL,
  `ename` char(10) NOT NULL,
  `shortname` char(4) NOT NULL,
  `url` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `yzy_type`
--

INSERT INTO `yzy_type` (`id`, `name`, `ename`, `shortname`, `url`) VALUES
(1, '百度网盘', 'dupan', '度盘', 'https:/pan.baidu.com/');

-- --------------------------------------------------------

--
-- 表的结构 `yzy_users`
--

CREATE TABLE `yzy_users` (
  `id` int(11) NOT NULL,
  `tid` tinyint(4) NOT NULL,
  `uid` varchar(20) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `avatar` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `yzy_class`
--
ALTER TABLE `yzy_class`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `yzy_resources`
--
ALTER TABLE `yzy_resources`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `yzy_type`
--
ALTER TABLE `yzy_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `yzy_users`
--
ALTER TABLE `yzy_users`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `yzy_class`
--
ALTER TABLE `yzy_class`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- 使用表AUTO_INCREMENT `yzy_resources`
--
ALTER TABLE `yzy_resources`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `yzy_type`
--
ALTER TABLE `yzy_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- 使用表AUTO_INCREMENT `yzy_users`
--
ALTER TABLE `yzy_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
