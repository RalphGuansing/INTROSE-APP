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
-- Table structure for table `accounts_payable`
--

DROP TABLE IF EXISTS `accounts_payable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_payable` (
  `date` datetime NOT NULL,
  `name` varchar(100) NOT NULL,
  `id_apv` int(11) NOT NULL,
  `amount` decimal(13,2) DEFAULT '0.00',
  PRIMARY KEY (`id_apv`),
  UNIQUE KEY `apv_id_UNIQUE` (`id_apv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_payable`
--

LOCK TABLES `accounts_payable` WRITE;
/*!40000 ALTER TABLE `accounts_payable` DISABLE KEYS */;
INSERT INTO `accounts_payable` VALUES ('0001-01-01 00:00:00','Caveman',1,246.00),('2017-12-08 00:00:00','Ralph EDITED2 Guansing',5,32500.00),('2017-12-09 00:00:00','John Doe',911,70000.00),('2017-12-09 00:00:00','Antoc namee',987,30000.00),('2017-12-09 00:00:00','Gott tom namee',988,45000.00),('2017-12-05 00:00:00','Ralph Guansing',1234,250.00),('2017-11-29 00:00:00','Ralph Guansing',2023,30000.00),('2017-12-03 00:00:00','Ralph Guansing',2121,50000.00),('2017-12-03 00:00:00','Ralph Guansing',2122,2500.00),('2017-12-25 00:00:00','Ralph Guansing',2123,15000.00),('2017-11-26 00:00:00','Ralph Vincent C. Guansing',2198,32500.00),('2017-11-29 00:00:00','Ralph Vincent C. Guansing',2199,85.75),('2017-11-27 00:00:00','Kiefer Chong',2300,69000.00),('2017-12-05 00:00:00','Ralph Guansing',2424,500.00),('2017-11-27 00:00:00','Jarod Martinez',2600,32000.00),('2017-11-28 00:00:00','Jericho Dienzo',3017,100000.00),('2017-12-04 00:00:00','Kiefer Chong',3123,59000.00),('2017-12-02 00:00:00','Ralph Guansing',4152,32500.00),('2017-12-09 22:26:42','sky flakes',4153,123.00);
/*!40000 ALTER TABLE `accounts_payable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_receivable`
--

DROP TABLE IF EXISTS `accounts_receivable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_receivable` (
  `customer_id` int(11) NOT NULL,
  `receive_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `inv_id` int(11) NOT NULL,
  `amount` decimal(13,2) DEFAULT NULL,
  `date_paid` datetime DEFAULT NULL,
  `pr_id` int(11) DEFAULT NULL,
  `payment` decimal(13,2) DEFAULT NULL,
  PRIMARY KEY (`receive_id`),
  KEY `fk_customer_id_idx` (`customer_id`),
  CONSTRAINT `fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_receivable`
--

LOCK TABLES `accounts_receivable` WRITE;
/*!40000 ALTER TABLE `accounts_receivable` DISABLE KEYS */;
INSERT INTO `accounts_receivable` VALUES (1,1,'2017-12-08 00:00:00',2198,500.98,NULL,NULL,NULL),(1,2,'2017-12-09 00:00:00',2199,600.00,NULL,NULL,NULL),(2,3,'2017-12-09 00:00:00',2200,2000.00,'2017-12-09 00:00:00',35,2000.00),(1,4,'2017-12-09 00:00:00',2201,1352.55,'2017-12-09 00:00:00',321,1352.55),(2,5,'2017-12-07 00:00:00',3254,5496.23,NULL,NULL,NULL),(2,6,'2017-12-07 00:00:00',3255,98200.50,NULL,NULL,NULL),(2,7,'2017-12-08 00:00:00',3256,3567.55,'2017-12-09 00:00:00',98,3567.55);
/*!40000 ALTER TABLE `accounts_receivable` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Table structure for table `book keeping`
--

DROP TABLE IF EXISTS `book keeping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book keeping` (
  `idbook keeping` int(11) NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,0) NOT NULL DEFAULT '0',
  `nonvat` decimal(10,0) DEFAULT '0',
  `innumber` decimal(10,0) DEFAULT NULL,
  `customer` varchar(45) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`idbook keeping`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book keeping`
--

LOCK TABLES `book keeping` WRITE;
/*!40000 ALTER TABLE `book keeping` DISABLE KEYS */;
/*!40000 ALTER TABLE `book keeping` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `column_group`
--

LOCK TABLES `column_group` WRITE;
/*!40000 ALTER TABLE `column_group` DISABLE KEYS */;
INSERT INTO `column_group` VALUES (1,'Personal'),(2,'Government'),(3,'Expense'),(4,'Office'),(5,'test');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `column_name_table`
--

LOCK TABLES `column_name_table` WRITE;
/*!40000 ALTER TABLE `column_name_table` DISABLE KEYS */;
INSERT INTO `column_name_table` VALUES (1,1,'Meals and Snacks'),(2,1,'Gas and Oil'),(3,2,'Input Tax'),(4,2,'Output Tax Payable'),(5,1,'Bills'),(6,1,'Medical Expenses'),(12,1,'Tuition Fee'),(13,3,'Delivery Expense'),(14,3,'Advertising Expense'),(15,3,'Food Expense'),(17,4,'Office Supplies'),(18,1,'Miscellaneous'),(19,4,'Purchases Vatable'),(20,5,'test');
/*!40000 ALTER TABLE `column_name_table` ENABLE KEYS */;
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
  `component_unit` varchar(45) NOT NULL,
  `component_quantity` int(11) NOT NULL,
  `component_origprice` decimal(13,2) NOT NULL,
  `component_unitprice` decimal(13,2) NOT NULL,
  `component_amount` decimal(13,2) NOT NULL,
  `component_nonvat` decimal(13,2) NOT NULL,
  `component_vat` decimal(13,2) NOT NULL,
  `component_taxable` decimal(13,2) NOT NULL,
  `component_profit` decimal(13,2) NOT NULL,
  PRIMARY KEY (`idcomponent`),
  KEY `component_invoicenum_idx` (`component_invoicenum`),
  CONSTRAINT `component_invoicenum` FOREIGN KEY (`component_invoicenum`) REFERENCES `invoice` (`idinvoice`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `component`
--

LOCK TABLES `component` WRITE;
/*!40000 ALTER TABLE `component` DISABLE KEYS */;
INSERT INTO `component` VALUES (27,23,'Joliswu','jolilent',15,39.00,49.00,735.00,0.00,78.75,656.25,617.25);
/*!40000 ALTER TABLE `component` ENABLE KEYS */;
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
  CONSTRAINT `fk_id_apv` FOREIGN KEY (`id_apv`) REFERENCES `accounts_payable` (`id_apv`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit_type`
--

LOCK TABLES `credit_type` WRITE;
/*!40000 ALTER TABLE `credit_type` DISABLE KEYS */;
INSERT INTO `credit_type` VALUES (1,2198,'Meals and Snacks',16250.00),(2,2198,'Gas and Oil',16250.00),(3,2300,'Meals and Snacks',34500.00),(4,2300,'Gas and Oil',34500.00),(5,2600,'Gas and Oil',16000.00),(6,2600,'Meals and Snacks',16000.00),(7,3017,'Meals and Snacks',55000.00),(8,3017,'Gas and Oil',45000.00),(9,2199,'Meals and Snacks',85.75),(10,1,'Meals and Snacks',123.00),(11,1,'Gas and Oil',123.00),(12,2023,'Meals and Snacks',15000.00),(13,2023,'Input Tax',15000.00),(14,4152,'Meals and Snacks',8125.00),(15,4152,'Tuition Fee',8125.00),(16,4152,'Input Tax',8125.00),(17,4152,'Advertising Expense',8125.00),(18,2121,'Delivery Expense',25000.00),(19,2121,'Food Expense',25000.00),(20,2122,'Meals and Snacks',2500.00),(21,2123,'Tuition Fee',15000.00),(22,3123,'Meals and Snacks',9000.00),(23,3123,'Miscellaneous',50000.00),(24,1234,'Meals and Snacks',250.00),(25,2424,'Meals and Snacks',250.00),(26,2424,'Gas and Oil',250.00),(81,911,'Tuition Fee',70000.00),(82,987,'Tuition Fee',30000.00),(83,988,'Delivery Expense',15000.00),(84,988,'Advertising Expense',15000.00),(85,988,'Food Expense',15000.00);
/*!40000 ALTER TABLE `credit_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(100) NOT NULL,
  `address` varchar(150) NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Kingsroad vet','Cabanatuan City'),(2,'Ralph Guansing','24, Sumandig, San Ildefonso, Bulacan'),(3,'Hericho','6969 delozol st'),(4,'jenzo','912 vape lord st');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2300 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (2121,'netlabuser','netlab','user','61908d55f150bc445a19d756773d249567eafc81'),(2299,'Ralph2198','Ralph','Guansing','5c4aadc115ba13aa20b71f7c5ca6c455297acb99');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_type`
--

DROP TABLE IF EXISTS `employee_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee_type` (
  `id_element` int(11) NOT NULL AUTO_INCREMENT,
  `employee_id` int(11) NOT NULL,
  `employee_role` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_element`),
  KEY `fk_employee_id_idx` (`employee_id`),
  CONSTRAINT `fk_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_type`
--

LOCK TABLES `employee_type` WRITE;
/*!40000 ALTER TABLE `employee_type` DISABLE KEYS */;
INSERT INTO `employee_type` VALUES (1,2299,'Accountant'),(2,2299,'Inventory'),(3,2121,'Accounting'),(4,2121,'Inventory');
/*!40000 ALTER TABLE `employee_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventory` (
  `idinventory` int(11) NOT NULL AUTO_INCREMENT,
  `productName` varchar(45) NOT NULL,
  `supplier` varchar(45) DEFAULT NULL,
  `packagingType` varchar(45) DEFAULT NULL,
  `perunitprice` float NOT NULL,
  `retailprice` float NOT NULL,
  `quantity` int(11) NOT NULL,
  `lastupdated` datetime DEFAULT NULL,
  `vatable` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`idinventory`),
  UNIQUE KEY `idinventory_UNIQUE` (`idinventory`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (20,'sky flakes','my sans','bag',123,10,11,'2017-12-09 22:26:42',1);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
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
  `invoice_date` varchar(45) NOT NULL,
  `invoice_term` enum('30 Days',' 60 Days','90 Days') NOT NULL,
  `invoice_ddate` varchar(45) NOT NULL,
  `invoice_amount` decimal(13,2) NOT NULL,
  `invoice_nonvat` decimal(13,2) NOT NULL,
  `invoice_vat` decimal(13,2) NOT NULL,
  `invoice_taxable` decimal(13,2) NOT NULL,
  `invoice_profit` decimal(13,2) NOT NULL,
  PRIMARY KEY (`idinvoice`),
  KEY `invoice_buyer_idx` (`invoice_buyer`),
  KEY `invoice_seller_idx` (`invoice_seller`),
  CONSTRAINT `invoice_buyer` FOREIGN KEY (`invoice_buyer`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `invoice_seller` FOREIGN KEY (`invoice_seller`) REFERENCES `agent` (`idagent`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice`
--

LOCK TABLES `invoice` WRITE;
/*!40000 ALTER TABLE `invoice` DISABLE KEYS */;
INSERT INTO `invoice` VALUES (23,3,6,'2017-12-08 23:32:16','30 Days','2018-01-07 23:32:16',735.00,0.00,78.75,656.25,617.25);
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

-- Dump completed on 2017-12-11  0:25:24
