USE `jeecg-boot`;
#1
/*
DROP TABLE IF EXISTS `dwgk`;
CREATE TABLE `dwgk`(`id` int(10) PRIMARY KEY,`title` varchar(200),`href` varchar(200),`datetime` varchar(100));

DROP TABLE IF EXISTS `gsgg`;
CREATE TABLE `gsgg`(`id` int(10) PRIMARY KEY,`title` varchar(200),`href` varchar(200),`datetime` varchar(100));

DROP TABLE IF EXISTS `pxjy`;
CREATE TABLE `pxjy`(`id` int(10) PRIMARY KEY,`title` varchar(200),`href` varchar(200),`datetime` varchar(100));

DROP TABLE IF EXISTS `zcfg`;
CREATE TABLE `zcfg`(`id` int(10) PRIMARY KEY,`title` varchar(200),`href` varchar(200),`datetime` varchar(100));

DROP TABLE IF EXISTS `zfbzgs`;
CREATE TABLE `zfbzgs`(`id` int(10) PRIMARY KEY,`title` varchar(200),`href` varchar(200),`datetime` varchar(100));

DROP TABLE IF EXISTS `zjdt`;
CREATE TABLE `zjdt`(`id` int(10) PRIMARY KEY,`title` varchar(200),`href` varchar(200),`datetime` varchar(100));

#2
DROP TABLE IF EXISTS `zfxxgk`;
CREATE TABLE `zfxxgk`(`column` varchar(200), `sub_column` varchar(200),`title` varchar(200),`href` varchar(200),`datetime` datetime);


CREATE TABLE `zqzl`(`column` varchar(100),`title` varchar(200),`href` varchar(200),`datetime` datetime);
*/

DROP TABLE IF EXISTS `articles`;
CREATE TABLE `articles`  (
  `id` INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
  `lanmu` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '栏目',
  `sub_lanmu` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '子栏目',
  `title` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '标题',
  `href` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '链接',
  `release_date` datetime NULL DEFAULT NULL COMMENT '发布日期'
  
  );
