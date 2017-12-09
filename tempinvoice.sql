CREATE DATABASE  IF NOT EXISTS `lcg_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `lcg_db`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: lcg_db
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
-- Table structure for table `agent`
--

DROP TABLE IF EXISTS `agent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agent` (
  `idagent` int(11) NOT NULL AUTO_INCREMENT,
  `agent_name` varchar(45) NOT NULL,
  `agent_quota` decimal(13,2) unsigned zerofill DEFAULT NULL,
  PRIMARY KEY (`idagent`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agent`
--

LOCK TABLES `agent` WRITE;
/*!40000 ALTER TABLE `agent` DISABLE KEYS */;
INSERT INTO `agent` VALUES (5,'Jringas',00000000690.00),(6,'Fanalili',00000000420.00);
/*!40000 ALTER TABLE `agent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `idclient` int(11) NOT NULL AUTO_INCREMENT,
  `client_name` varchar(45) NOT NULL,
  `client_address` varchar(45) NOT NULL,
  PRIMARY KEY (`idclient`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (3,'Hericho','6969 delozol st'),(4,'jenzo','912 vape lord st');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `idcompany` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(45) NOT NULL,
  `company_address` varchar(45) NOT NULL,
  PRIMARY KEY (`idcompany`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'ratbu.inc','123 yeet blvd'),(2,'plague.inc','678 bolijee');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `component`
--

DROP TABLE IF EXISTS `component`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `component` (
  `idcomponent` int(11) NOT NULL AUTO_INCREMENT,
  `component_invoicenum` int(11) NOT NULL,
  `component_name` varchar(100) NOT NULL,
  `component_quantity` int(11) NOT NULL,
  `component_origprice` decimal(13,2) NOT NULL,
  `component_unitprice` decimal(13,2) NOT NULL,
  PRIMARY KEY (`idcomponent`),
  KEY `component_invoicenum_idx` (`component_invoicenum`),
  CONSTRAINT `component_invoicenum` FOREIGN KEY (`component_invoicenum`) REFERENCES `invoice` (`idinvoice`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `component`
--

LOCK TABLES `component` WRITE;
/*!40000 ALTER TABLE `component` DISABLE KEYS */;
INSERT INTO `component` VALUES (12,12,'Jolispag',32,59.00,69.00),(15,15,'Joliswu',15,39.00,49.00),(16,15,'Jolidog',25,29.00,39.00);
/*!40000 ALTER TABLE `component` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice`
--

DROP TABLE IF EXISTS `invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invoice` (
  `idinvoice` int(11) NOT NULL AUTO_INCREMENT,
  `invoice_buyer` int(11) NOT NULL,
  `invoice_seller` int(11) NOT NULL,
  `invoice_date` datetime NOT NULL,
  `invoice_term` enum('Cash on Delivery','30 Days',' 60 Days','90 Days') NOT NULL,
  `invoice_ddate` datetime NOT NULL,
  `invoice_amount` decimal(13,2) NOT NULL,
  `invoice_nonvat` decimal(13,2) NOT NULL,
  `invoice_vat` decimal(13,2) NOT NULL,
  `invoice_taxable` decimal(13,2) NOT NULL,
  PRIMARY KEY (`idinvoice`),
  KEY `invoice_buyer_idx` (`invoice_buyer`),
  KEY `invoice_seller_idx` (`invoice_seller`),
  CONSTRAINT `invoice_buyer` FOREIGN KEY (`invoice_buyer`) REFERENCES `client` (`idclient`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `invoice_seller` FOREIGN KEY (`invoice_seller`) REFERENCES `agent` (`idagent`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice`
--

LOCK TABLES `invoice` WRITE;
/*!40000 ALTER TABLE `invoice` DISABLE KEYS */;
INSERT INTO `invoice` VALUES (12,4,5,'2017-12-07 20:45:53','30 Days','2018-01-06 20:45:53',660.00,120.00,20.00,250.00),(15,3,6,'2017-12-08 08:10:07','30 Days','2018-01-07 08:10:07',990.00,200.00,15.00,300.00);
/*!40000 ALTER TABLE `invoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `idproduct` int(11) NOT NULL AUTO_INCREMENT,
  `product_supplier` int(11) NOT NULL,
  `product_quantity` int(10) unsigned zerofill NOT NULL,
  `product_unit` varchar(45) DEFAULT NULL,
  `product_name` varchar(45) NOT NULL,
  `product_price` float NOT NULL,
  PRIMARY KEY (`idproduct`),
  KEY `product_supplier_idx` (`product_supplier`),
  CONSTRAINT `product_supplier` FOREIGN KEY (`product_supplier`) REFERENCES `company` (`idcompany`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-08 14:38:05
