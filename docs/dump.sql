-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: soccer_island
-- ------------------------------------------------------
-- Server version	5.5.40-0ubuntu0.14.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add classification',7,'add_classification'),(20,'Can change classification',7,'change_classification'),(21,'Can delete classification',7,'delete_classification'),(22,'Can add address',8,'add_address'),(23,'Can change address',8,'change_address'),(24,'Can delete address',8,'delete_address'),(25,'Can add suspension',9,'add_suspension'),(26,'Can change suspension',9,'change_suspension'),(27,'Can delete suspension',9,'delete_suspension'),(28,'Can add person',10,'add_person'),(29,'Can change person',10,'change_person'),(30,'Can delete person',10,'delete_person'),(31,'Can add club',11,'add_club'),(32,'Can change club',11,'change_club'),(33,'Can delete club',11,'delete_club'),(34,'Can add play for',12,'add_playfor'),(35,'Can change play for',12,'change_playfor'),(36,'Can delete play for',12,'delete_playfor'),(37,'Can add team',13,'add_team'),(38,'Can change team',13,'change_team'),(39,'Can delete team',13,'delete_team'),(40,'Can add player',14,'add_player'),(41,'Can change player',14,'change_player'),(42,'Can delete player',14,'delete_player'),(43,'Can add coach',15,'add_coach'),(44,'Can change coach',15,'change_coach'),(45,'Can delete coach',15,'delete_coach'),(46,'Can add coach for',16,'add_coachfor'),(47,'Can change coach for',16,'change_coachfor'),(48,'Can delete coach for',16,'delete_coachfor'),(49,'Can add referee',17,'add_referee'),(50,'Can change referee',17,'change_referee'),(51,'Can delete referee',17,'delete_referee'),(52,'Can add field',18,'add_field'),(53,'Can change field',18,'change_field'),(54,'Can delete field',18,'delete_field'),(55,'Can add competition',19,'add_competition'),(56,'Can change competition',19,'change_competition'),(57,'Can delete competition',19,'delete_competition'),(58,'Can add season',20,'add_season'),(59,'Can change season',20,'change_season'),(60,'Can delete season',20,'delete_season'),(61,'Can add matchday',21,'add_matchday'),(62,'Can change matchday',21,'change_matchday'),(63,'Can delete matchday',21,'delete_matchday'),(64,'Can add goal',22,'add_goal'),(65,'Can change goal',22,'change_goal'),(66,'Can delete goal',22,'delete_goal'),(67,'Can add game',23,'add_game'),(68,'Can change game',23,'change_game'),(69,'Can delete game',23,'delete_game'),(70,'Can add card',24,'add_card'),(71,'Can change card',24,'change_card'),(72,'Can delete card',24,'delete_card');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$cukQgoLWkKus$a9mzUqgDSvPGlmzQpNLgREtDE8Jq1A1sArNiXA9Thrg=','2014-12-06 03:35:04',1,'root','','','r@root.com',1,1,'2014-11-13 07:45:21');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-11-13 07:56:27','1','Legends',1,'',7,1),(2,'2014-11-13 07:57:08','2','Men\'s Open',1,'',7,1),(3,'2014-11-13 07:57:23','1','Men\'s Open Legends of Football',1,'',19,1),(4,'2014-11-13 07:58:25','1','Team 1970s',1,'',13,1),(5,'2014-11-13 07:58:45','2','Team 1980s',1,'',13,1),(6,'2014-11-13 07:59:06','3','Team 1990s',1,'',13,1),(7,'2014-11-13 07:59:24','4','Team 2000s',1,'',13,1),(8,'2014-11-13 07:59:33','1','Men\'s Open Legends of Football - 2014-2015',1,'',20,1),(9,'2014-11-13 08:00:08','1','Matchday1',1,'',21,1),(10,'2014-11-13 08:00:37','2','Matchday 2',1,'',21,1),(11,'2014-11-13 08:01:51','1','Waipio Soccer Complex: Field 1',1,'',18,1),(12,'2014-11-13 08:02:04','1','Team 1980s vs Team 1970s (2014-09-01 12:00:00-10:00)',1,'',23,1),(13,'2014-11-13 08:02:33','2','Team 2000s vs Team 1990s (2014-09-01 12:00:00-10:00)',1,'',23,1),(14,'2014-11-13 08:02:58','3','Team 1990s vs Team 1970s (2014-12-01 12:00:00-10:00)',1,'',23,1),(15,'2014-11-13 08:03:22','4','Team 2000s vs Team 1980s (2014-12-01 12:00:00-10:00)',1,'',23,1),(16,'2014-11-13 08:04:04','1','Franz Beckenbauer at Team 1970s',1,'',12,1),(17,'2014-11-13 08:04:23','2','Diego Maradona at Team 1980s',1,'',12,1),(18,'2014-11-13 08:04:47','3','Edson do Nascimento at Team 1970s',1,'',12,1),(19,'2014-11-13 08:05:07','4','Johan Cruijff at Team 1970s',1,'',12,1),(20,'2014-11-13 08:05:25','5','Lionel Messi at Team 2000s',1,'',12,1),(21,'2014-11-13 08:05:47','6','Ronaldo de Lima at Team 1990s',1,'',12,1),(22,'2014-11-13 08:06:04','7','Zinedine Zidane at Team 2000s',1,'',12,1),(23,'2014-11-13 08:06:23','8','Marco van Basten at Team 1990s',1,'',12,1),(24,'2014-11-13 08:06:41','9','Michael Laudrup at Team 1990s',1,'',12,1),(25,'2014-11-13 08:06:59','10','Eric Cantona at Team 1990s',1,'',12,1),(26,'2014-11-13 08:07:12','11','Thierry Henry at Team 2000s',1,'',12,1),(27,'2014-11-13 08:07:29','12','Lothar Matthäus at Team 1990s',1,'',12,1),(28,'2014-11-13 08:07:50','13','Francesco Totti at Team 2000s',1,'',12,1),(29,'2014-11-13 08:08:05','14','George Best at Team 1970s',1,'',12,1),(30,'2014-11-13 08:08:21','15','Eusébio da Silva Ferreira at Team 1970s',1,'',12,1),(31,'2014-11-13 08:08:36','16','Oliver Kahn at Team 2000s',1,'',12,1),(32,'2014-11-13 08:08:51','17','Peter Schmeichel at Team 1990s',1,'',12,1),(33,'2014-11-13 08:09:04','18','Roberto Carlos at Team 2000s',1,'',12,1),(34,'2014-11-13 08:09:28','3','Edson do Nascimento at Team 1970s',2,'Changed number.',12,1),(35,'2014-11-13 08:09:38','15','Eusébio da Silva Ferreira at Team 1970s',2,'Changed number.',12,1),(36,'2014-11-13 08:09:55','5','Lionel Messi at Team 2000s',2,'Changed number.',12,1),(37,'2014-11-13 08:11:12','2','Team 2000s vs Team 1990s (2014-09-01 12:00:00-10:00)',2,'Changed played.',23,1),(38,'2014-11-13 08:12:37','14','George Best',2,'Changed position.',14,1),(39,'2014-11-13 08:12:44','12','Lothar Matthäus',2,'Changed position.',14,1),(40,'2014-11-13 08:13:44','11','Thierry Henry',2,'Changed position.',14,1),(41,'2014-11-13 08:14:05','14','George Best',2,'No fields changed.',14,1),(42,'2014-11-13 08:14:13','15','Eusébio da Silva Ferreira',2,'Changed position.',14,1),(43,'2014-11-13 08:14:58','5','Lionel Messi at Team 2000s',2,'Changed number.',12,1),(44,'2014-11-13 08:16:22','1','Franz Beckenbauer Team 1990s',1,'',16,1),(45,'2014-11-13 08:16:52','2','Jose Mourinho Team 2000s',1,'',16,1),(46,'2014-11-13 08:17:07','1','Franz Beckenbauer Team 1980s',2,'Changed team.',16,1),(47,'2014-11-13 08:17:25','3','Johan Cruijff Team 1990s',1,'',16,1),(48,'2014-11-13 08:17:41','4','Ottmar Hitzfeld Team 1970s',1,'',16,1),(49,'2014-11-13 08:18:26','2','Jose Mourinho Team 2000s',2,'Changed responsibility.',16,1),(50,'2014-11-13 08:18:46','5','Ottmar Hitzfeld Team 2000s',1,'',16,1),(51,'2014-11-13 08:19:03','5','Ottmar Hitzfeld Team 2000s',2,'Changed responsibility.',16,1),(52,'2014-11-13 08:35:19','1','Y Card (Nonemin)',1,'',24,1),(53,'2014-11-13 08:35:44','2','R Card (Nonemin)',1,'',24,1),(54,'2014-11-13 08:36:10','3','Y Card (Nonemin)',1,'',24,1),(55,'2014-11-13 08:36:27','4','Y Card (Nonemin)',1,'',24,1),(56,'2014-11-13 08:38:10','3','R Card (Nonemin)',2,'Changed color.',24,1),(57,'2014-11-13 23:14:58','1','Team 1980s vs Team 1970s (2014-09-01 22:00:00+00:00) Nonemin',1,'',22,1),(58,'2014-11-13 23:15:29','2','Team 1980s vs Team 1970s (2014-09-01 22:00:00+00:00) Nonemin',1,'',22,1),(59,'2014-11-13 23:15:51','3','Team 1980s vs Team 1970s (2014-09-01 22:00:00+00:00) Nonemin',1,'',22,1),(60,'2014-11-13 23:16:02','4','Team 1980s vs Team 1970s (2014-09-01 22:00:00+00:00) Nonemin',1,'',22,1),(61,'2014-11-13 23:16:47','5','Team 2000s vs Team 1990s (2014-09-01 22:00:00+00:00) Nonemin',1,'',22,1),(62,'2014-11-13 23:17:13','6','Team 2000s vs Team 1990s (2014-09-01 22:00:00+00:00) Nonemin',1,'',22,1),(63,'2014-11-13 23:17:37','7','Team 2000s vs Team 1990s (2014-09-01 22:00:00+00:00) Nonemin',1,'',22,1),(64,'2014-11-13 23:18:08','8','Team 2000s vs Team 1990s (2014-09-01 22:00:00+00:00) Nonemin',1,'',22,1),(65,'2014-11-13 23:18:36','9','Team 2000s vs Team 1990s (2014-09-01 22:00:00+00:00) Nonemin',1,'',22,1),(66,'2014-11-14 01:47:51','2','Matchday 3',2,'Changed label.',21,1),(67,'2014-11-14 01:48:07','3','Matchday 2',1,'',21,1),(68,'2014-11-14 01:48:57','5','Team 1970s vs Team 2000s (2014-10-15 12:00:00-10:00)',1,'',23,1),(69,'2014-11-14 01:49:28','6','Team 1980s vs Team 1990s (2014-10-15 12:00:00-10:00)',1,'',23,1),(70,'2014-11-14 01:50:34','8','Marco van Basten at Team 1990s',2,'Changed to_date.',12,1),(71,'2014-11-14 01:51:04','19','Marco van Basten at Team 1980s',1,'',12,1),(72,'2014-11-15 22:47:25','1','Eric Cantona 2014-11-01',1,'',9,1),(73,'2014-11-15 23:07:00','2','Legends Cup (Men\'s Open)',1,'',19,1),(74,'2014-11-15 23:08:12','2','2014-2015 Legends Cup (Men\'s Open)',1,'',20,1),(75,'2014-11-15 23:09:14','4','Semi-finals',1,'',21,1),(76,'2014-11-15 23:09:56','5','Final',1,'',21,1),(77,'2014-11-15 23:11:08','7','Team 1980s vs Team 1970s (2014-11-01 12:00:00-10:00)',1,'',23,1),(78,'2014-11-15 23:11:33','8','Team 2000s vs Team 1990s (2014-11-01 12:00:00-10:00)',1,'',23,1),(79,'2014-11-15 23:12:28','9','Team 1990s vs Team 1970s (2015-05-01 12:00:00-10:00)',1,'',23,1),(80,'2014-11-15 23:32:22','2','Men\'s Open',2,'Changed slug.',7,1),(81,'2014-11-16 02:43:19','1','Legends',3,'',7,1),(82,'2014-11-17 01:55:58','1','Team 1980s vs Team 1970s (2014-09-01 12:00:00-10:00)',2,'Changed scored_by for goal \"Team 1980s vs Team 1970s (2014-09-01 12:00:00-10:00) Nonemin\".',23,1),(83,'2014-11-22 00:08:09','1','2014-2015 Legends of Football (Men\'s Open)',2,'Changed published.',20,1),(84,'2014-11-23 23:23:11','1','Eric Cantona 2014-11-01',2,'Changed suspended_until and reason.',9,1),(85,'2014-11-23 23:39:02','1','Eric Cantona 2014-11-01',2,'Changed competition.',9,1),(86,'2014-11-23 23:52:00','1','Eric Cantona 2014-11-01',2,'Changed competition.',9,1),(87,'2014-11-23 23:53:41','1','Eric Cantona 2014-11-01',2,'No fields changed.',9,1),(88,'2014-11-23 23:56:26','1','Eric Cantona 2014-11-01',2,'Changed fine.',9,1),(89,'2014-11-24 00:06:27','1','Eric Cantona 2014-11-01',2,'Changed fine_paid.',9,1),(90,'2014-12-04 19:22:41','6','Matchday 4',1,'',21,1),(91,'2014-12-06 02:19:39','1','Matchday 1',2,'Changed label.',21,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'classification','stats','classification'),(8,'address','stats','address'),(9,'suspension','stats','suspension'),(10,'person','stats','person'),(11,'club','stats','club'),(12,'play for','stats','playfor'),(13,'team','stats','team'),(14,'player','stats','player'),(15,'coach','stats','coach'),(16,'coach for','stats','coachfor'),(17,'referee','stats','referee'),(18,'field','stats','field'),(19,'competition','stats','competition'),(20,'season','stats','season'),(21,'matchday','stats','matchday'),(22,'goal','stats','goal'),(23,'game','stats','game'),(24,'card','stats','card');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2014-11-13 07:43:52'),(2,'auth','0001_initial','2014-11-13 07:43:52'),(3,'admin','0001_initial','2014-11-13 07:43:53'),(4,'sessions','0001_initial','2014-11-13 07:43:53'),(5,'stats','0001_initial','2014-11-13 07:43:57'),(6,'stats','0002_auto_20141106_1156','2014-11-13 07:43:57'),(7,'stats','0003_auto_20141106_1200','2014-11-13 07:43:58'),(8,'stats','0004_auto_20141106_2156','2014-11-13 07:43:58'),(9,'stats','0005_auto_20141106_2156','2014-11-13 07:43:58'),(10,'stats','0006_auto_20141107_1514','2014-11-13 07:43:59'),(11,'stats','0007_auto_20141107_2222','2014-11-13 07:43:59'),(12,'stats','0008_suspension_season','2014-11-13 07:44:00'),(13,'stats','0009_auto_20141108_0918','2014-11-13 07:44:00'),(14,'stats','0010_auto_20141108_1955','2014-11-13 07:44:01'),(15,'stats','0011_auto_20141108_2112','2014-11-13 07:44:02'),(16,'stats','0012_matchday_end_date','2014-11-13 07:44:02'),(17,'stats','0013_remove_matchday_end_date','2014-11-13 07:44:02'),(18,'stats','0014_auto_20141109_0849','2014-11-13 07:44:03'),(19,'stats','0015_auto_20141109_0911','2014-11-13 07:44:04'),(20,'stats','0016_remove_suspension_number_games','2014-11-13 07:44:04'),(21,'stats','0017_auto_20141109_1033','2014-11-13 07:44:05'),(22,'stats','0018_auto_20141109_1106','2014-11-13 07:44:05'),(23,'stats','0019_auto_20141109_1207','2014-11-13 07:44:06'),(24,'stats','0020_auto_20141109_1220','2014-11-13 07:44:07'),(25,'stats','0021_auto_20141111_1831','2014-11-13 07:44:08'),(26,'stats','0022_auto_20141112_1908','2014-11-13 07:44:09'),(27,'stats','0023_auto_20141112_2048','2014-11-13 07:44:10'),(28,'stats','0024_auto_20141112_2129','2014-11-13 07:44:10'),(29,'stats','0025_auto_20141112_2143','2014-11-13 07:44:11'),(30,'stats','0026_auto_20141119_1119','2014-11-19 21:19:54'),(31,'stats','0027_auto_20141119_1146','2014-11-20 19:57:03'),(32,'stats','0028_auto_20141120_0956','2014-11-20 19:57:03'),(33,'stats','0029_season_published','2014-11-22 00:02:56'),(34,'stats','0030_field_about','2014-11-22 05:14:11'),(35,'stats','0031_auto_20141123_1337','2014-11-23 23:37:42');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('43twt3uiyx7o18jkrx9z6qsx9egqehya','ZTc0OTY2ZmM2NmFhNWUwMTNjZTc2NWMzZjk3NmE0NWYxMGRlNzljODp7fQ==','2014-12-07 21:22:42'),('4fjscgmbn33bir3ubywd30i404cq864s','ZTc0OTY2ZmM2NmFhNWUwMTNjZTc2NWMzZjk3NmE0NWYxMGRlNzljODp7fQ==','2014-12-07 22:08:16'),('8f5ckv6qm987dhew526aokxat4sd20sj','ZTc0OTY2ZmM2NmFhNWUwMTNjZTc2NWMzZjk3NmE0NWYxMGRlNzljODp7fQ==','2014-12-04 06:31:10'),('9atks63ky8f3cz1l345x41fdt96yf0jc','ZTc0OTY2ZmM2NmFhNWUwMTNjZTc2NWMzZjk3NmE0NWYxMGRlNzljODp7fQ==','2014-12-18 19:23:23'),('ea2xhu5522dtp1imlz9u4ry449ty72e6','ZTc0OTY2ZmM2NmFhNWUwMTNjZTc2NWMzZjk3NmE0NWYxMGRlNzljODp7fQ==','2014-12-04 06:18:31'),('msdu6h1siqg0x6s52x44swcgh4kn5b7t','ZTc0OTY2ZmM2NmFhNWUwMTNjZTc2NWMzZjk3NmE0NWYxMGRlNzljODp7fQ==','2014-12-20 03:37:13'),('spk71nwpgeel092pthfuzdqo42q5vjmf','ZTc0OTY2ZmM2NmFhNWUwMTNjZTc2NWMzZjk3NmE0NWYxMGRlNzljODp7fQ==','2014-12-07 21:34:23'),('y9vfefde8j8ey1dnx0v4l678h5u4rcz3','ZTc0OTY2ZmM2NmFhNWUwMTNjZTc2NWMzZjk3NmE0NWYxMGRlNzljODp7fQ==','2014-12-04 21:52:27');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_address`
--

DROP TABLE IF EXISTS `stats_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `street` varchar(128) NOT NULL,
  `city` varchar(64) NOT NULL,
  `state` varchar(2) NOT NULL,
  `zip_code` varchar(16) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `email` varchar(75) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_address`
--

LOCK TABLES `stats_address` WRITE;
/*!40000 ALTER TABLE `stats_address` DISABLE KEYS */;
INSERT INTO `stats_address` VALUES (1,'Kalakaua Avenue','Honolulu','HI','968','808 000 0000','josemorinho@mail.com'),(2,'Kapiolani Blvd','Honolulu','HI','968','808 111 1111','ottmarhitzfeld@mail.com'),(3,'Waipo','Honolulu','HI','968','','');
/*!40000 ALTER TABLE `stats_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_card`
--

DROP TABLE IF EXISTS `stats_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_card` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `minute` smallint(6) DEFAULT NULL,
  `color` varchar(1) NOT NULL,
  `in_game_id` int(11) DEFAULT NULL,
  `play_for_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stats_card_def6ee40` (`in_game_id`),
  KEY `stats_card_2db86204` (`play_for_id`),
  CONSTRAINT `stats_card_in_game_id_29b040e7f6b9da35_fk_stats_game_id` FOREIGN KEY (`in_game_id`) REFERENCES `stats_game` (`id`),
  CONSTRAINT `stats_card_play_for_id_658a5787a55d7698_fk_stats_playfor_id` FOREIGN KEY (`play_for_id`) REFERENCES `stats_playfor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_card`
--

LOCK TABLES `stats_card` WRITE;
/*!40000 ALTER TABLE `stats_card` DISABLE KEYS */;
INSERT INTO `stats_card` VALUES (1,67,'Y',1,1),(2,NULL,'R',2,7),(3,NULL,'R',2,10),(4,NULL,'Y',2,10),(5,3,'Y',1,4);
/*!40000 ALTER TABLE `stats_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_classification`
--

DROP TABLE IF EXISTS `stats_classification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_classification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `label` varchar(32) NOT NULL,
  `slug` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_classification`
--

LOCK TABLES `stats_classification` WRITE;
/*!40000 ALTER TABLE `stats_classification` DISABLE KEYS */;
INSERT INTO `stats_classification` VALUES (2,'Men\'s Open','mens-open');
/*!40000 ALTER TABLE `stats_classification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_club`
--

DROP TABLE IF EXISTS `stats_club`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_club` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `slug` varchar(64) NOT NULL,
  `address_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  UNIQUE KEY `stats_club_name_5c260801f34a1886_uniq` (`name`),
  KEY `stats_club_ea8e5d12` (`address_id`),
  CONSTRAINT `stats_club_address_id_6846fe0254819089_fk_stats_address_id` FOREIGN KEY (`address_id`) REFERENCES `stats_address` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_club`
--

LOCK TABLES `stats_club` WRITE;
/*!40000 ALTER TABLE `stats_club` DISABLE KEYS */;
/*!40000 ALTER TABLE `stats_club` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_coach`
--

DROP TABLE IF EXISTS `stats_coach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_coach` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`),
  CONSTRAINT `stats_coach_person_id_3bcd3e0b059cb78a_fk_stats_person_id` FOREIGN KEY (`person_id`) REFERENCES `stats_person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_coach`
--

LOCK TABLES `stats_coach` WRITE;
/*!40000 ALTER TABLE `stats_coach` DISABLE KEYS */;
INSERT INTO `stats_coach` VALUES (3,1),(4,4),(1,20),(2,21);
/*!40000 ALTER TABLE `stats_coach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_coachfor`
--

DROP TABLE IF EXISTS `stats_coachfor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_coachfor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_date` date NOT NULL,
  `to_date` date DEFAULT NULL,
  `responsibility` varchar(1) DEFAULT NULL,
  `coach_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stats_coachfor_ea814e95` (`coach_id`),
  KEY `stats_coachfor_f6a7ca40` (`team_id`),
  CONSTRAINT `stats_coachfor_coach_id_41e4215015b93ccc_fk_stats_coach_id` FOREIGN KEY (`coach_id`) REFERENCES `stats_coach` (`id`),
  CONSTRAINT `stats_coachfor_team_id_587d585348391910_fk_stats_team_id` FOREIGN KEY (`team_id`) REFERENCES `stats_team` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_coachfor`
--

LOCK TABLES `stats_coachfor` WRITE;
/*!40000 ALTER TABLE `stats_coachfor` DISABLE KEYS */;
INSERT INTO `stats_coachfor` VALUES (1,'2014-09-01',NULL,'C',3,2),(2,'2014-09-01',NULL,'M',1,4),(3,'2014-09-01',NULL,'C',4,3),(4,'2014-09-01',NULL,'C',2,1),(5,'2014-09-01',NULL,'C',2,4);
/*!40000 ALTER TABLE `stats_coachfor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_competition`
--

DROP TABLE IF EXISTS `stats_competition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_competition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `slug` varchar(64) NOT NULL,
  `mode` varchar(1) NOT NULL,
  `classification_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stats_competition_2dbcba41` (`slug`),
  KEY `stats_competition_946aa2ca` (`classification_id`),
  CONSTRAINT `st_classification_id_7f5c3bc1890c3cc0_fk_stats_classification_id` FOREIGN KEY (`classification_id`) REFERENCES `stats_classification` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_competition`
--

LOCK TABLES `stats_competition` WRITE;
/*!40000 ALTER TABLE `stats_competition` DISABLE KEYS */;
INSERT INTO `stats_competition` VALUES (1,'Legends of Football','legends-of-football','L',2),(2,'Legends Cup','legends-cup','C',2);
/*!40000 ALTER TABLE `stats_competition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_field`
--

DROP TABLE IF EXISTS `stats_field`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_field` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `slug` varchar(64) NOT NULL,
  `address_id` int(11) NOT NULL,
  `about` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `stats_field_ea8e5d12` (`address_id`),
  CONSTRAINT `stats_field_address_id_37ebfde016c42162_fk_stats_address_id` FOREIGN KEY (`address_id`) REFERENCES `stats_address` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_field`
--

LOCK TABLES `stats_field` WRITE;
/*!40000 ALTER TABLE `stats_field` DISABLE KEYS */;
INSERT INTO `stats_field` VALUES (1,'Waipio Soccer Complex: Field 1','waipio-soccer-complex-field-1-waipo-968',3,'');
/*!40000 ALTER TABLE `stats_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_game`
--

DROP TABLE IF EXISTS `stats_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_game` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `name` varchar(64) NOT NULL,
  `away_team_id` int(11) DEFAULT NULL,
  `field_id` int(11) NOT NULL,
  `home_team_id` int(11) DEFAULT NULL,
  `matchday_id` int(11) NOT NULL,
  `next_game_id` int(11) DEFAULT NULL,
  `referee_id` int(11) DEFAULT NULL,
  `played` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stats_game_901b4047` (`away_team_id`),
  KEY `stats_game_3aabf39f` (`field_id`),
  KEY `stats_game_e5623f1e` (`home_team_id`),
  KEY `stats_game_9f35f176` (`matchday_id`),
  KEY `stats_game_efa3f36d` (`next_game_id`),
  KEY `stats_game_3cf09080` (`referee_id`),
  CONSTRAINT `stats_game_away_team_id_30e966ad7cee71e1_fk_stats_team_id` FOREIGN KEY (`away_team_id`) REFERENCES `stats_team` (`id`),
  CONSTRAINT `stats_game_field_id_7864b5a2584fd2b1_fk_stats_field_id` FOREIGN KEY (`field_id`) REFERENCES `stats_field` (`id`),
  CONSTRAINT `stats_game_home_team_id_7bfd9c06946665f0_fk_stats_team_id` FOREIGN KEY (`home_team_id`) REFERENCES `stats_team` (`id`),
  CONSTRAINT `stats_game_matchday_id_5f0d938ee1a8ad49_fk_stats_matchday_id` FOREIGN KEY (`matchday_id`) REFERENCES `stats_matchday` (`id`),
  CONSTRAINT `stats_game_next_game_id_34a322f8184d117f_fk_stats_game_id` FOREIGN KEY (`next_game_id`) REFERENCES `stats_game` (`id`),
  CONSTRAINT `stats_game_referee_id_796ef95bea597d9_fk_stats_referee_id` FOREIGN KEY (`referee_id`) REFERENCES `stats_referee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_game`
--

LOCK TABLES `stats_game` WRITE;
/*!40000 ALTER TABLE `stats_game` DISABLE KEYS */;
INSERT INTO `stats_game` VALUES (1,'2014-09-01 22:00:00','',1,1,2,1,NULL,1,1),(2,'2014-09-02 00:00:00','',3,1,4,1,NULL,1,1),(3,'2014-12-01 22:00:00','',1,1,3,2,NULL,1,0),(4,'2014-12-01 22:00:00','',2,1,4,2,NULL,1,0),(5,'2014-10-15 22:00:00','',4,1,1,3,NULL,1,1),(6,'2014-10-15 22:00:00','',3,1,2,3,NULL,1,1),(7,'2014-11-01 22:00:00','',1,1,2,4,NULL,1,1),(8,'2014-11-01 22:00:00','',3,1,4,4,NULL,1,0),(9,'2015-05-01 22:00:00','',1,1,3,5,NULL,1,0);
/*!40000 ALTER TABLE `stats_game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_goal`
--

DROP TABLE IF EXISTS `stats_goal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_goal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `minute` smallint(6) DEFAULT NULL,
  `assisted_by_id` int(11) DEFAULT NULL,
  `scored_by_id` int(11) DEFAULT NULL,
  `scored_for_id` int(11) NOT NULL,
  `game_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stats_goal_fbf76cfd` (`assisted_by_id`),
  KEY `stats_goal_75a7163c` (`scored_by_id`),
  KEY `stats_goal_cb446227` (`scored_for_id`),
  KEY `stats_goal_8e9c7365` (`game_id`),
  CONSTRAINT `stats_goal_assisted_by_id_7b7a804a2bc4ff80_fk_stats_playfor_id` FOREIGN KEY (`assisted_by_id`) REFERENCES `stats_playfor` (`id`),
  CONSTRAINT `stats_goal_game_id_367e61e90c154db9_fk_stats_game_id` FOREIGN KEY (`game_id`) REFERENCES `stats_game` (`id`),
  CONSTRAINT `stats_goal_scored_by_id_2dca7b348d791a96_fk_stats_playfor_id` FOREIGN KEY (`scored_by_id`) REFERENCES `stats_playfor` (`id`),
  CONSTRAINT `stats_goal_scored_for_id_db647aa03f2e9c7_fk_stats_team_id` FOREIGN KEY (`scored_for_id`) REFERENCES `stats_team` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_goal`
--

LOCK TABLES `stats_goal` WRITE;
/*!40000 ALTER TABLE `stats_goal` DISABLE KEYS */;
INSERT INTO `stats_goal` VALUES (1,30,4,3,1,1),(2,90,1,3,1,1),(3,23,NULL,2,2,1),(4,73,NULL,2,2,1),(5,0,7,11,4,2),(6,0,18,7,4,2),(7,0,7,13,4,2),(8,0,10,8,3,2),(9,0,9,6,3,2),(11,0,2,19,2,6),(34,0,9,6,3,6),(43,0,NULL,2,2,6),(44,0,NULL,2,2,6),(45,0,NULL,6,3,3),(46,3,NULL,2,2,1);
/*!40000 ALTER TABLE `stats_goal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_matchday`
--

DROP TABLE IF EXISTS `stats_matchday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_matchday` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slug` varchar(32) DEFAULT NULL,
  `season_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `label` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stats_matchday_2dbcba41` (`slug`),
  KEY `stats_matchday_b11701f0` (`season_id`),
  CONSTRAINT `stats_matchday_season_id_4f6a3705d464f68e_fk_stats_season_id` FOREIGN KEY (`season_id`) REFERENCES `stats_season` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_matchday`
--

LOCK TABLES `stats_matchday` WRITE;
/*!40000 ALTER TABLE `stats_matchday` DISABLE KEYS */;
INSERT INTO `stats_matchday` VALUES (1,'matchday-1',1,'2014-09-01','Matchday 1'),(2,'matchday-3',1,'2014-12-01','Matchday 3'),(3,'matchday-2',1,'2014-10-15','Matchday 2'),(4,'semi-finals',2,'2014-11-01','Semi-finals'),(5,'final',2,'2015-05-01','Final'),(6,'matchday-4',1,'2015-02-01','Matchday 4');
/*!40000 ALTER TABLE `stats_matchday` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_person`
--

DROP TABLE IF EXISTS `stats_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(64) NOT NULL,
  `middle_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(1) NOT NULL,
  `address_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stats_person_ea8e5d12` (`address_id`),
  CONSTRAINT `stats_person_address_id_723582a4ef700afe_fk_stats_address_id` FOREIGN KEY (`address_id`) REFERENCES `stats_address` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_person`
--

LOCK TABLES `stats_person` WRITE;
/*!40000 ALTER TABLE `stats_person` DISABLE KEYS */;
INSERT INTO `stats_person` VALUES (1,'Franz','','Beckenbauer',NULL,'M',NULL),(2,'Diego','','Maradona',NULL,'M',NULL),(3,'Edson','','do Nascimento',NULL,'M',NULL),(4,'Johan','','Cruijff',NULL,'M',NULL),(5,'Lionel','','Messi',NULL,'M',NULL),(6,'Ronaldo','','de Lima',NULL,'M',NULL),(7,'Zinedine','','Zidane',NULL,'M',NULL),(8,'Marco','','van Basten',NULL,'M',NULL),(9,'Michael','','Laudrup',NULL,'M',NULL),(10,'Eric','','Cantona',NULL,'M',NULL),(11,'Thierry','','Henry',NULL,'M',NULL),(12,'Lothar','','Matthäus',NULL,'M',NULL),(13,'Francesco','','Totti',NULL,'M',NULL),(14,'George','','Best',NULL,'M',NULL),(15,'Eusébio','','da Silva Ferreira',NULL,'M',NULL),(16,'Pierluigi','','Collina',NULL,'M',NULL),(17,'Oliver','','Kahn',NULL,'M',NULL),(18,'Peter','','Schmeichel',NULL,'M',NULL),(19,'Roberto','','Carlos',NULL,'M',NULL),(20,'Jose','','Mourinho',NULL,'M',1),(21,'Ottmar','','Hitzfeld',NULL,'M',2);
/*!40000 ALTER TABLE `stats_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_player`
--

DROP TABLE IF EXISTS `stats_player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_player` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `about` varchar(1024) NOT NULL,
  `position` varchar(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`),
  CONSTRAINT `stats_player_person_id_321b1b86a96534cc_fk_stats_person_id` FOREIGN KEY (`person_id`) REFERENCES `stats_person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_player`
--

LOCK TABLES `stats_player` WRITE;
/*!40000 ALTER TABLE `stats_player` DISABLE KEYS */;
INSERT INTO `stats_player` VALUES (1,1,'','M'),(2,2,'','M'),(3,3,'','F'),(4,4,'','M'),(5,5,'','F'),(6,6,'','F'),(7,7,'','M'),(8,8,'','F'),(9,9,'','M'),(10,10,'','F'),(11,11,'','F'),(12,12,'','M'),(13,13,'','F'),(14,14,'','F'),(15,15,'','F'),(16,17,'','G'),(17,18,'','G'),(18,19,'','D');
/*!40000 ALTER TABLE `stats_player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_playfor`
--

DROP TABLE IF EXISTS `stats_playfor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_playfor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_date` date NOT NULL,
  `to_date` date DEFAULT NULL,
  `player_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  `injury_reserve` tinyint(1) NOT NULL,
  `number` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stats_playfor_afe72417` (`player_id`),
  KEY `stats_playfor_f6a7ca40` (`team_id`),
  CONSTRAINT `stats_playfor_player_id_3c0ca8cbf5129d3f_fk_stats_player_id` FOREIGN KEY (`player_id`) REFERENCES `stats_player` (`id`),
  CONSTRAINT `stats_playfor_team_id_4302a18993221e1f_fk_stats_team_id` FOREIGN KEY (`team_id`) REFERENCES `stats_team` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_playfor`
--

LOCK TABLES `stats_playfor` WRITE;
/*!40000 ALTER TABLE `stats_playfor` DISABLE KEYS */;
INSERT INTO `stats_playfor` VALUES (1,'2014-09-01',NULL,1,1,0,4),(2,'2014-09-01',NULL,2,2,0,10),(3,'2014-09-01',NULL,3,1,0,10),(4,'2014-09-01',NULL,4,1,0,14),(5,'2014-09-01',NULL,5,4,0,11),(6,'2014-09-01',NULL,6,3,0,9),(7,'2014-09-01',NULL,7,4,0,10),(8,'2014-09-01','2014-10-01',8,3,0,12),(9,'2014-09-01',NULL,9,3,0,10),(10,'2014-09-01',NULL,10,3,0,7),(11,'2014-09-01',NULL,11,4,0,14),(12,'2014-09-01',NULL,12,3,0,8),(13,'2014-09-01',NULL,13,4,0,9),(14,'2014-09-01',NULL,14,1,0,7),(15,'2014-09-01',NULL,15,1,0,9),(16,'2014-09-01',NULL,16,4,0,1),(17,'2014-09-01',NULL,17,3,0,1),(18,'2014-09-01',NULL,18,4,0,3),(19,'2014-10-01',NULL,8,2,1,12);
/*!40000 ALTER TABLE `stats_playfor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_referee`
--

DROP TABLE IF EXISTS `stats_referee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_referee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`),
  CONSTRAINT `stats_referee_person_id_6f8b3b6a22267f0a_fk_stats_person_id` FOREIGN KEY (`person_id`) REFERENCES `stats_person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_referee`
--

LOCK TABLES `stats_referee` WRITE;
/*!40000 ALTER TABLE `stats_referee` DISABLE KEYS */;
INSERT INTO `stats_referee` VALUES (1,16);
/*!40000 ALTER TABLE `stats_referee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_season`
--

DROP TABLE IF EXISTS `stats_season`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_season` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `label` varchar(9) DEFAULT NULL,
  `slug` varchar(9) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `competition_id` int(11) NOT NULL,
  `published` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stats_season_2dbcba41` (`slug`),
  KEY `stats_season_88606bbe` (`competition_id`),
  CONSTRAINT `stats_se_competition_id_251413d948a917d1_fk_stats_competition_id` FOREIGN KEY (`competition_id`) REFERENCES `stats_competition` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_season`
--

LOCK TABLES `stats_season` WRITE;
/*!40000 ALTER TABLE `stats_season` DISABLE KEYS */;
INSERT INTO `stats_season` VALUES (1,'2014-2015','2014-2015','2014-09-01','2015-05-31',1,1),(2,'2014-2015','2014-2015','2014-09-01','2015-05-31',2,0);
/*!40000 ALTER TABLE `stats_season` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_season_enrolled`
--

DROP TABLE IF EXISTS `stats_season_enrolled`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_season_enrolled` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `season_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `season_id` (`season_id`,`team_id`),
  KEY `stats_season_enrolled_b11701f0` (`season_id`),
  KEY `stats_season_enrolled_f6a7ca40` (`team_id`),
  CONSTRAINT `stats_season_enrolled_team_id_42ef71903b77e6b7_fk_stats_team_id` FOREIGN KEY (`team_id`) REFERENCES `stats_team` (`id`),
  CONSTRAINT `stats_season_enrol_season_id_3f8228a1ca5434f1_fk_stats_season_id` FOREIGN KEY (`season_id`) REFERENCES `stats_season` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_season_enrolled`
--

LOCK TABLES `stats_season_enrolled` WRITE;
/*!40000 ALTER TABLE `stats_season_enrolled` DISABLE KEYS */;
INSERT INTO `stats_season_enrolled` VALUES (9,1,1),(10,1,2),(11,1,3),(12,1,4),(5,2,1),(6,2,2),(7,2,3),(8,2,4);
/*!40000 ALTER TABLE `stats_season_enrolled` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_suspension`
--

DROP TABLE IF EXISTS `stats_suspension`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_suspension` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_received` date DEFAULT NULL,
  `suspended_until` date DEFAULT NULL,
  `reason` varchar(1024) NOT NULL,
  `fine` smallint(6) NOT NULL,
  `fine_paid` tinyint(1) NOT NULL,
  `player_id` int(11) NOT NULL,
  `competition_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stats_suspension_afe72417` (`player_id`),
  KEY `stats_suspension_88606bbe` (`competition_id`),
  CONSTRAINT `stats_su_competition_id_4795279813147d09_fk_stats_competition_id` FOREIGN KEY (`competition_id`) REFERENCES `stats_competition` (`id`),
  CONSTRAINT `stats_suspension_player_id_1e43e4fe392d9324_fk_stats_player_id` FOREIGN KEY (`player_id`) REFERENCES `stats_player` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_suspension`
--

LOCK TABLES `stats_suspension` WRITE;
/*!40000 ALTER TABLE `stats_suspension` DISABLE KEYS */;
INSERT INTO `stats_suspension` VALUES (1,'2014-11-01','2015-01-01','Assault on fan.',50,1,10,NULL);
/*!40000 ALTER TABLE `stats_suspension` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats_team`
--

DROP TABLE IF EXISTS `stats_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stats_team` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `slug` varchar(64) NOT NULL,
  `colors` varchar(128) NOT NULL,
  `classification_id` int(11) NOT NULL,
  `club_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `stats_team_946aa2ca` (`classification_id`),
  KEY `stats_team_7115697a` (`club_id`),
  CONSTRAINT `stats_team_club_id_5837c0f04cf87d9f_fk_stats_club_id` FOREIGN KEY (`club_id`) REFERENCES `stats_club` (`id`),
  CONSTRAINT `st_classification_id_66428990c9aca321_fk_stats_classification_id` FOREIGN KEY (`classification_id`) REFERENCES `stats_classification` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats_team`
--

LOCK TABLES `stats_team` WRITE;
/*!40000 ALTER TABLE `stats_team` DISABLE KEYS */;
INSERT INTO `stats_team` VALUES (1,'Team 1970s','team-1970s','red',2,NULL),(2,'Team 1980s','team-1980s','Blue',2,NULL),(3,'Team 1990s','team-1990s','green',2,NULL),(4,'Team 2000s','team-2000s','yellow',2,NULL);
/*!40000 ALTER TABLE `stats_team` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-05 17:39:02
