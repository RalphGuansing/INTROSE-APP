CREATE DATABASE  IF NOT EXISTS `introse` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `introse`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: introse
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `column_group`
--

DROP TABLE IF EXISTS `column_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `column_group` (
  `id_group` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id_group`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `column_group`
--

LOCK TABLES `column_group` WRITE;
/*!40000 ALTER TABLE `column_group` DISABLE KEYS */;
INSERT INTO `column_group` VALUES (1,'Personal'),(2,'Government'),(3,'Expense');
/*!40000 ALTER TABLE `column_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `column_name_table`
--

DROP TABLE IF EXISTS `column_name_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `column_name_table` (
  `id_column` int(11) NOT NULL AUTO_INCREMENT,
  `id_group` int(11) NOT NULL,
  `column_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id_column`),
  KEY `fk_id_group_idx` (`id_group`),
  CONSTRAINT `fk_id_group` FOREIGN KEY (`id_group`) REFERENCES `column_group` (`id_group`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `column_name_table`
--

LOCK TABLES `column_name_table` WRITE;
/*!40000 ALTER TABLE `column_name_table` DISABLE KEYS */;
INSERT INTO `column_name_table` VALUES (1,1,'Meals and Snacks'),(2,1,'Gas and Oil'),(3,2,'Input Tax'),(4,2,'Output Tax Payable'),(5,1,'Bills'),(6,1,'Medical Expenses'),(12,1,'Tuition Fee'),(13,3,'Delivery Expense'),(14,3,'Advertising Expense');
/*!40000 ALTER TABLE `column_name_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credit_type`
--

DROP TABLE IF EXISTS `credit_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credit_type` (
  `id_element` int(11) NOT NULL AUTO_INCREMENT,
  `id_apv` int(11) NOT NULL,
  `type_name` varchar(100) DEFAULT NULL,
  `type_value` decimal(13,2) DEFAULT NULL,
  PRIMARY KEY (`id_element`),
  KEY `fk_id_apv_idx` (`id_apv`),
  CONSTRAINT `fk_id_apv` FOREIGN KEY (`id_apv`) REFERENCES `vouchers payable` (`id_apv`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit_type`
--

LOCK TABLES `credit_type` WRITE;
/*!40000 ALTER TABLE `credit_type` DISABLE KEYS */;
INSERT INTO `credit_type` VALUES (1,2198,'Meals and Snacks',16250.00),(2,2198,'Gas and Oil',16250.00),(3,2300,'Meals and Snacks',34500.00),(4,2300,'Gas and Oil',34500.00),(5,2600,'Gas and Oil',16000.00),(6,2600,'Meals and Snacks',16000.00),(7,3017,'Meals and Snacks',55000.00),(8,3017,'Gas and Oil',45000.00),(9,2199,'Meals and Snacks',85.75),(10,1,'Meals and Snacks',123.00),(11,1,'Gas and Oil',123.00),(12,2023,'Meals and Snacks',15000.00),(13,2023,'Input Tax',15000.00),(14,4152,'Meals and Snacks',8125.00),(15,4152,'Tuition Fee',8125.00),(16,4152,'Input Tax',8125.00),(17,4152,'Advertising Expense',8125.00);
/*!40000 ALTER TABLE `credit_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventory` (
  `inventory_id` int(11) NOT NULL,
  `product_name` varchar(45) NOT NULL,
  `supplier` varchar(45) DEFAULT NULL,
  `unit` varchar(45) DEFAULT NULL,
  `unit_price` float NOT NULL,
  `quantity` int(11) NOT NULL,
  `lastupdated` datetime DEFAULT NULL,
  PRIMARY KEY (`inventory_id`),
  UNIQUE KEY `inventory_id_UNIQUE` (`inventory_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,'AMBIFLUD 20 KILOS','Aces','bag',2400,10,'2017-11-05 00:00:00'),(2,'AMBIFLUD 20 KILOS','Aces','bag',2400.45,10,'2017-11-05 00:00:00');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vouchers payable`
--

DROP TABLE IF EXISTS `vouchers payable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vouchers payable` (
  `date` datetime NOT NULL,
  `name` varchar(100) NOT NULL,
  `id_apv` int(11) NOT NULL,
  `amount` decimal(13,2) DEFAULT '0.00',
  PRIMARY KEY (`id_apv`),
  UNIQUE KEY `apv_id_UNIQUE` (`id_apv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vouchers payable`
--

LOCK TABLES `vouchers payable` WRITE;
/*!40000 ALTER TABLE `vouchers payable` DISABLE KEYS */;
INSERT INTO `vouchers payable` VALUES ('0001-01-01 00:00:00','Caveman',1,246.00),('2017-11-29 00:00:00','Ralph Guansing',2023,30000.00),('2017-11-26 00:00:00','Ralph Vincent C. Guansing',2198,32500.00),('2017-11-29 00:00:00','Ralph Vincent C. Guansing',2199,85.75),('2017-11-27 00:00:00','Kiefer Chong',2300,69000.00),('2017-11-27 00:00:00','Jarod Martinez',2600,32000.00),('2017-11-28 00:00:00','Jericho Dienzo',3017,100000.00),('2017-12-02 00:00:00','Ralph Guansing',4152,32500.00);
/*!40000 ALTER TABLE `vouchers payable` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-02 16:10:39
