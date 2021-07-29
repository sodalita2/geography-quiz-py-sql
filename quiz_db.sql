-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: quiz_db
-- ------------------------------------------------------
-- Server version	8.0.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cities` (
  `id_cities` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `id_countries` int NOT NULL,
  PRIMARY KEY (`id_cities`),
  KEY `id_countries_idx` (`id_countries`),
  CONSTRAINT `id_countries` FOREIGN KEY (`id_countries`) REFERENCES `countries` (`id_countries`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES (1,'Bangkok',3),(3,'Rio de Janeiro',2),(4,'Sao Paulo',2),(9,'Chiang Mai',3),(10,'Marseille',4),(11,'Lyon',4),(12,'Lille',4),(14,'Leipzig',5),(15,'Dortmund',5),(16,'Frankfurt',5),(17,'Berlin',5),(18,'Baghdad',6),(19,'Beijing',7),(20,'Shanghai',7),(21,'Wuhan',7),(22,'Bogotá',8),(23,'Cali',8),(24,'Bratislavia',9),(25,'Budapest',10),(26,'Buenos Aires',11),(27,'Canberra',12),(28,'Melbourne',12),(29,'Cairo',13),(30,'Copenhagen',14),(31,'Lagos',15),(32,'Dublin',16),(33,'Havana',17),(34,'Jakarta',18),(35,'Surabaya',18),(36,'Bandung',18),(37,'Kampala',19),(38,'Kyiv',20),(39,'Lisbon',21),(40,'Madrid',22),(41,'Manila',23),(42,'Montevideo',24),(43,'Ottawa',25),(44,'Prague',26),(45,'Rome',27),(46,'Abu Dhabi',28),(47,'Belgrade',29),(48,'Bucharest',30),(49,'Brussels',31),(50,'Damascus',32),(51,'Helsinki',33),(52,'Lima',34),(53,'Monrovia',35),(55,'New Delhi',36),(56,'Pyongyang',37),(57,'Seoul',38),(58,'Stockholm',39),(59,'Tokyo',40),(60,'Osaka',40),(61,'Tehran',41),(62,'Warsaw',42),(63,'Tunis',43),(64,'Incheon',38);
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `continents`
--

DROP TABLE IF EXISTS `continents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `continents` (
  `id_continents` int NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id_continents`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `continents`
--

LOCK TABLES `continents` WRITE;
/*!40000 ALTER TABLE `continents` DISABLE KEYS */;
INSERT INTO `continents` VALUES (1,'Europe'),(2,'Asia'),(3,'North America'),(4,'South America'),(5,'Africa'),(6,'Oceania'),(7,'Antarctica');
/*!40000 ALTER TABLE `continents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `countries` (
  `id_countries` int NOT NULL AUTO_INCREMENT,
  `id_continents` int NOT NULL,
  `capital` varchar(30) NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id_countries`),
  KEY `id_continents_idx` (`id_continents`),
  CONSTRAINT `id_continents` FOREIGN KEY (`id_continents`) REFERENCES `continents` (`id_continents`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (2,4,'Brasilia','Brazil'),(3,2,'Bangkok','Thailand'),(4,1,'Paris','France'),(5,1,'Berlin','Germany'),(6,2,'Baghdad','Iraq'),(7,2,'Beijing','China'),(8,4,'Bogotá','Colombia'),(9,1,'Bratislava','Slovakia'),(10,1,'Budapest','Hungary'),(11,4,'Buenos Aires','Argentina'),(12,6,'Canberra','Australia'),(13,5,'Cairo','Egypt'),(14,1,'Copenhagen','Denmark'),(15,5,'Lagos','Nigeria'),(16,1,'Dublin','Ireland'),(17,3,'Havana','Cuba'),(18,2,'Jakarta','Indonesia'),(19,5,'Kampala','Uganda'),(20,1,'Kyiv','Ukraine'),(21,1,'Lisbon','Portugal'),(22,1,'Madrid','Spain'),(23,2,'Manila','Philippines'),(24,4,'Montevideo','Uruguay'),(25,3,'Ottawa','Canada'),(26,1,'Prague','Czech Republic'),(27,1,'Rome','Italy'),(28,2,'Abu Dhabi','UAE'),(29,1,'Belgrade','Serbia'),(30,1,'Bucharest','Romania'),(31,1,'Brussels','Belgium'),(32,2,'Damascus','Syria'),(33,1,'Helsinki','Finland'),(34,4,'Lima','Peru'),(35,5,'Monrovia','Liberia'),(36,2,'New Delhi','India'),(37,2,'Pyongyang','North Korea'),(38,1,'Stockholm','Sweden'),(39,2,'Seoul','South Korea'),(40,2,'Tokyo','Japan'),(41,2,'Tehran','Iran'),(42,1,'Warsaw','Poland'),(43,5,'Tunis','Tunisia');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-28 18:06:00
