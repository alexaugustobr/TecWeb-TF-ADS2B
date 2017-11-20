
USE localdb;
-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: 192.168.1.162    Database: localdb
-- ------------------------------------------------------
-- Server version	5.7.19-0ubuntu0.16.04.1

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
-- Table structure for table `Aluno`
--

DROP TABLE IF EXISTS `Aluno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Aluno` (
  `usuario_ptr_id` int(11) NOT NULL,
  `celular` varchar(11) DEFAULT NULL,
  `curso_id` int(11) NOT NULL,
  `foto_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`usuario_ptr_id`),
  KEY `Aluno_curso_id_74ab1773_fk_Curso_id` (`curso_id`),
  KEY `Aluno_foto_id_4ad2beec_fk_ArquivosFoto_id` (`foto_id`),
  CONSTRAINT `Aluno_curso_id_74ab1773_fk_Curso_id` FOREIGN KEY (`curso_id`) REFERENCES `Curso` (`id`),
  CONSTRAINT `Aluno_foto_id_4ad2beec_fk_ArquivosFoto_id` FOREIGN KEY (`foto_id`) REFERENCES `ArquivosFoto` (`id`),
  CONSTRAINT `Aluno_usuario_ptr_id_11d10b0e_fk_Usuario_id` FOREIGN KEY (`usuario_ptr_id`) REFERENCES `Usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Aluno`
--

LOCK TABLES `Aluno` WRITE;
/*!40000 ALTER TABLE `Aluno` DISABLE KEYS */;
/*!40000 ALTER TABLE `Aluno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ArquivosFoto`
--

DROP TABLE IF EXISTS `ArquivosFoto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ArquivosFoto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `arquivo` varchar(10000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ArquivosFoto`
--

LOCK TABLES `ArquivosFoto` WRITE;
/*!40000 ALTER TABLE `ArquivosFoto` DISABLE KEYS */;
/*!40000 ALTER TABLE `ArquivosFoto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ArquivosQuestao`
--

DROP TABLE IF EXISTS `ArquivosQuestao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ArquivosQuestao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `arquivo` varchar(500) NOT NULL,
  `questao_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ArquivosQuestao_questao_id_39754589_fk_Questao_id` (`questao_id`),
  CONSTRAINT `ArquivosQuestao_questao_id_39754589_fk_Questao_id` FOREIGN KEY (`questao_id`) REFERENCES `Questao` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ArquivosQuestao`
--

LOCK TABLES `ArquivosQuestao` WRITE;
/*!40000 ALTER TABLE `ArquivosQuestao` DISABLE KEYS */;
/*!40000 ALTER TABLE `ArquivosQuestao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ArquivosResposta`
--

DROP TABLE IF EXISTS `ArquivosResposta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ArquivosResposta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `arquivo` varchar(500) NOT NULL,
  `resposta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ArquivosResposta_resposta_id_f2b8a662_fk_Resposta_id` (`resposta_id`),
  CONSTRAINT `ArquivosResposta_resposta_id_f2b8a662_fk_Resposta_id` FOREIGN KEY (`resposta_id`) REFERENCES `Resposta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ArquivosResposta`
--

LOCK TABLES `ArquivosResposta` WRITE;
/*!40000 ALTER TABLE `ArquivosResposta` DISABLE KEYS */;
/*!40000 ALTER TABLE `ArquivosResposta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Candidado`
--

DROP TABLE IF EXISTS `Candidado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Candidado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(120) DEFAULT NULL,
  `ra` varchar(80) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `celular` varchar(11) DEFAULT NULL,
  `codigo_acesso` varchar(120) DEFAULT NULL,
  `matricula_aceita` tinyint(1) NOT NULL,
  `confirmado` tinyint(1) NOT NULL,
  `foto_id` int(11) DEFAULT NULL,
  `turma_id` int(11) DEFAULT NULL,
  `aluno_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Candidado_foto_id_96c02125_fk_ArquivosFoto_id` (`foto_id`),
  KEY `Candidado_turma_id_5befcac3_fk_Turma_id` (`turma_id`),
  KEY `Candidado_aluno_id_506fe92f_fk_Aluno_usuario_ptr_id` (`aluno_id`),
  CONSTRAINT `Candidado_aluno_id_506fe92f_fk_Aluno_usuario_ptr_id` FOREIGN KEY (`aluno_id`) REFERENCES `Aluno` (`usuario_ptr_id`),
  CONSTRAINT `Candidado_foto_id_96c02125_fk_ArquivosFoto_id` FOREIGN KEY (`foto_id`) REFERENCES `ArquivosFoto` (`id`),
  CONSTRAINT `Candidado_turma_id_5befcac3_fk_Turma_id` FOREIGN KEY (`turma_id`) REFERENCES `Turma` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Candidado`
--

LOCK TABLES `Candidado` WRITE;
/*!40000 ALTER TABLE `Candidado` DISABLE KEYS */;
/*!40000 ALTER TABLE `Candidado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Curso`
--

DROP TABLE IF EXISTS `Curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Curso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sigla` varchar(5) NOT NULL,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sigla` (`sigla`),
  UNIQUE KEY `nome` (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Curso`
--

LOCK TABLES `Curso` WRITE;
/*!40000 ALTER TABLE `Curso` DISABLE KEYS */;
/*!40000 ALTER TABLE `Curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CursoTurma`
--

DROP TABLE IF EXISTS `CursoTurma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CursoTurma` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `turma_id` int(11) NOT NULL,
  `curso_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `CursoTurma_turma_id_curso_id_7723c433_uniq` (`turma_id`,`curso_id`),
  KEY `CursoTurma_curso_id_aee9d168_fk_Curso_id` (`curso_id`),
  CONSTRAINT `CursoTurma_curso_id_aee9d168_fk_Curso_id` FOREIGN KEY (`curso_id`) REFERENCES `Curso` (`id`),
  CONSTRAINT `CursoTurma_turma_id_12eaad28_fk_Turma_id` FOREIGN KEY (`turma_id`) REFERENCES `Turma` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CursoTurma`
--

LOCK TABLES `CursoTurma` WRITE;
/*!40000 ALTER TABLE `CursoTurma` DISABLE KEYS */;
/*!40000 ALTER TABLE `CursoTurma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Disciplina`
--

DROP TABLE IF EXISTS `Disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Disciplina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(240) NOT NULL,
  `carga_horaria` smallint(6) NOT NULL,
  `teoria` decimal(3,2) NOT NULL,
  `pratica` decimal(3,2) NOT NULL,
  `ementa` longtext NOT NULL,
  `competencias` longtext NOT NULL,
  `habilidades` longtext NOT NULL,
  `conteudo` longtext NOT NULL,
  `bibliografia_complementar` longtext NOT NULL,
  `bibliografia_basica` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Disciplina`
--

LOCK TABLES `Disciplina` WRITE;
/*!40000 ALTER TABLE `Disciplina` DISABLE KEYS */;
/*!40000 ALTER TABLE `Disciplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DisciplinaOfertada`
--

DROP TABLE IF EXISTS `DisciplinaOfertada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DisciplinaOfertada` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ano` smallint(6) NOT NULL,
  `semestre` varchar(1) NOT NULL,
  `disciplina_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DisciplinaOfertada_disciplina_id_0d7cb697_fk_Disciplina_id` (`disciplina_id`),
  CONSTRAINT `DisciplinaOfertada_disciplina_id_0d7cb697_fk_Disciplina_id` FOREIGN KEY (`disciplina_id`) REFERENCES `Disciplina` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DisciplinaOfertada`
--

LOCK TABLES `DisciplinaOfertada` WRITE;
/*!40000 ALTER TABLE `DisciplinaOfertada` DISABLE KEYS */;
/*!40000 ALTER TABLE `DisciplinaOfertada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GradeCurricular`
--

DROP TABLE IF EXISTS `GradeCurricular`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GradeCurricular` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ano` smallint(6) NOT NULL,
  `semestre` varchar(1) NOT NULL,
  `curso_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GradeCurricular_curso_id_92730f1c_fk_Curso_id` (`curso_id`),
  CONSTRAINT `GradeCurricular_curso_id_92730f1c_fk_Curso_id` FOREIGN KEY (`curso_id`) REFERENCES `Curso` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GradeCurricular`
--

LOCK TABLES `GradeCurricular` WRITE;
/*!40000 ALTER TABLE `GradeCurricular` DISABLE KEYS */;
/*!40000 ALTER TABLE `GradeCurricular` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Matricula`
--

DROP TABLE IF EXISTS `Matricula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Matricula` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aluno_id` int(11) NOT NULL,
  `turma_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Matricula_aluno_id_turma_id_460cd5b1_uniq` (`aluno_id`,`turma_id`),
  KEY `Matricula_turma_id_262a5d60_fk_Turma_id` (`turma_id`),
  CONSTRAINT `Matricula_aluno_id_ef0199a0_fk_Aluno_usuario_ptr_id` FOREIGN KEY (`aluno_id`) REFERENCES `Aluno` (`usuario_ptr_id`),
  CONSTRAINT `Matricula_turma_id_262a5d60_fk_Turma_id` FOREIGN KEY (`turma_id`) REFERENCES `Turma` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Matricula`
--

LOCK TABLES `Matricula` WRITE;
/*!40000 ALTER TABLE `Matricula` DISABLE KEYS */;
/*!40000 ALTER TABLE `Matricula` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Periodo`
--

DROP TABLE IF EXISTS `Periodo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Periodo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero` smallint(6) NOT NULL,
  `gradeCurricular_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Periodo_gradeCurricular_id_e07688d0_fk_GradeCurricular_id` (`gradeCurricular_id`),
  CONSTRAINT `Periodo_gradeCurricular_id_e07688d0_fk_GradeCurricular_id` FOREIGN KEY (`gradeCurricular_id`) REFERENCES `GradeCurricular` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Periodo`
--

LOCK TABLES `Periodo` WRITE;
/*!40000 ALTER TABLE `Periodo` DISABLE KEYS */;
/*!40000 ALTER TABLE `Periodo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PeriodoDisicplina`
--

DROP TABLE IF EXISTS `PeriodoDisicplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PeriodoDisicplina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `periodo_id` int(11) NOT NULL,
  `disciplina_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `PeriodoDisicplina_periodo_id_disciplina_id_4d696e73_uniq` (`periodo_id`,`disciplina_id`),
  KEY `PeriodoDisicplina_disciplina_id_4fd67309_fk_Disciplina_id` (`disciplina_id`),
  CONSTRAINT `PeriodoDisicplina_disciplina_id_4fd67309_fk_Disciplina_id` FOREIGN KEY (`disciplina_id`) REFERENCES `Disciplina` (`id`),
  CONSTRAINT `PeriodoDisicplina_periodo_id_54aa0b41_fk_Periodo_id` FOREIGN KEY (`periodo_id`) REFERENCES `Periodo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PeriodoDisicplina`
--

LOCK TABLES `PeriodoDisicplina` WRITE;
/*!40000 ALTER TABLE `PeriodoDisicplina` DISABLE KEYS */;
/*!40000 ALTER TABLE `PeriodoDisicplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Professor`
--

DROP TABLE IF EXISTS `Professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Professor` (
  `usuario_ptr_id` int(11) NOT NULL,
  `apelido` varchar(30) DEFAULT NULL,
  `celular` varchar(11) NOT NULL,
  PRIMARY KEY (`usuario_ptr_id`),
  UNIQUE KEY `apelido` (`apelido`),
  CONSTRAINT `Professor_usuario_ptr_id_d7315225_fk_Usuario_id` FOREIGN KEY (`usuario_ptr_id`) REFERENCES `Usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Professor`
--

LOCK TABLES `Professor` WRITE;
/*!40000 ALTER TABLE `Professor` DISABLE KEYS */;
/*!40000 ALTER TABLE `Professor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Questao`
--

DROP TABLE IF EXISTS `Questao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Questao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` longtext NOT NULL,
  `data_limite_entrega` date NOT NULL,
  `numero` int(11) NOT NULL,
  `data` date NOT NULL,
  `turma_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Questao_turma_id_2697c4b4_fk_Turma_id` (`turma_id`),
  CONSTRAINT `Questao_turma_id_2697c4b4_fk_Turma_id` FOREIGN KEY (`turma_id`) REFERENCES `Turma` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Questao`
--

LOCK TABLES `Questao` WRITE;
/*!40000 ALTER TABLE `Questao` DISABLE KEYS */;
/*!40000 ALTER TABLE `Questao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Resposta`
--

DROP TABLE IF EXISTS `Resposta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Resposta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_avaliacao` date DEFAULT NULL,
  `nota` decimal(4,2) DEFAULT NULL,
  `avaliacao` longtext,
  `descricao` longtext NOT NULL,
  `data_de_envio` date NOT NULL,
  `questao_id` int(11) NOT NULL,
  `aluno_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Resposta_questao_id_85f566c5_fk_Questao_id` (`questao_id`),
  KEY `Resposta_aluno_id_0279393c_fk_Aluno_usuario_ptr_id` (`aluno_id`),
  CONSTRAINT `Resposta_aluno_id_0279393c_fk_Aluno_usuario_ptr_id` FOREIGN KEY (`aluno_id`) REFERENCES `Aluno` (`usuario_ptr_id`),
  CONSTRAINT `Resposta_questao_id_85f566c5_fk_Questao_id` FOREIGN KEY (`questao_id`) REFERENCES `Questao` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Resposta`
--

LOCK TABLES `Resposta` WRITE;
/*!40000 ALTER TABLE `Resposta` DISABLE KEYS */;
/*!40000 ALTER TABLE `Resposta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Turma`
--

DROP TABLE IF EXISTS `Turma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Turma` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `turno` varchar(15) NOT NULL,
  `turma_sigla` varchar(1) NOT NULL,
  `disciplinaOfertada_id` int(11) NOT NULL,
  `professor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Turma_disciplinaOfertada_id_df16d165_fk_DisciplinaOfertada_id` (`disciplinaOfertada_id`),
  KEY `Turma_professor_id_9202676b_fk_Professor_usuario_ptr_id` (`professor_id`),
  CONSTRAINT `Turma_disciplinaOfertada_id_df16d165_fk_DisciplinaOfertada_id` FOREIGN KEY (`disciplinaOfertada_id`) REFERENCES `DisciplinaOfertada` (`id`),
  CONSTRAINT `Turma_professor_id_9202676b_fk_Professor_usuario_ptr_id` FOREIGN KEY (`professor_id`) REFERENCES `Professor` (`usuario_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Turma`
--

LOCK TABLES `Turma` WRITE;
/*!40000 ALTER TABLE `Turma` DISABLE KEYS */;
/*!40000 ALTER TABLE `Turma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `last_login` datetime(6) DEFAULT NULL,
  `ra` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `ativo` tinyint(1) NOT NULL,
  `perfil` varchar(1) NOT NULL,
  `password` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ra` (`ra`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
INSERT INTO `Usuario` VALUES (1,'2017-11-19 21:20:39.000000',123456,'Admin','admin@handcode.com',1,'C','pbkdf2_sha256$36000$Be2EXve4yCqb$/06J85AYBf6ZOjynsrzyzo65TwxYvOsemDqPx32ceYg=');
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;

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
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
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
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add candidato',6,'add_candidato'),(17,'Can change candidato',6,'change_candidato'),(18,'Can delete candidato',6,'delete_candidato'),(19,'Can add curso',7,'add_curso'),(20,'Can change curso',7,'change_curso'),(21,'Can delete curso',7,'delete_curso'),(22,'Can add periodo',8,'add_periodo'),(23,'Can change periodo',8,'change_periodo'),(24,'Can delete periodo',8,'delete_periodo'),(25,'Can add questao',9,'add_questao'),(26,'Can change questao',9,'change_questao'),(27,'Can delete questao',9,'delete_questao'),(28,'Can add turma',10,'add_turma'),(29,'Can change turma',10,'change_turma'),(30,'Can delete turma',10,'delete_turma'),(31,'Can add arquivos foto',11,'add_arquivosfoto'),(32,'Can change arquivos foto',11,'change_arquivosfoto'),(33,'Can delete arquivos foto',11,'delete_arquivosfoto'),(34,'Can add arquivos resposta',12,'add_arquivosresposta'),(35,'Can change arquivos resposta',12,'change_arquivosresposta'),(36,'Can delete arquivos resposta',12,'delete_arquivosresposta'),(37,'Can add arquivos questao',13,'add_arquivosquestao'),(38,'Can change arquivos questao',13,'change_arquivosquestao'),(39,'Can delete arquivos questao',13,'delete_arquivosquestao'),(40,'Can add grade curricular',14,'add_gradecurricular'),(41,'Can change grade curricular',14,'change_gradecurricular'),(42,'Can delete grade curricular',14,'delete_gradecurricular'),(43,'Can add disciplina',15,'add_disciplina'),(44,'Can change disciplina',15,'change_disciplina'),(45,'Can delete disciplina',15,'delete_disciplina'),(46,'Can add usuario',16,'add_usuario'),(47,'Can change usuario',16,'change_usuario'),(48,'Can delete usuario',16,'delete_usuario'),(49,'Can add resposta',17,'add_resposta'),(50,'Can change resposta',17,'change_resposta'),(51,'Can delete resposta',17,'delete_resposta'),(52,'Can add disciplina ofertada',18,'add_disciplinaofertada'),(53,'Can change disciplina ofertada',18,'change_disciplinaofertada'),(54,'Can delete disciplina ofertada',18,'delete_disciplinaofertada'),(55,'Can add aluno',19,'add_aluno'),(56,'Can change aluno',19,'change_aluno'),(57,'Can delete aluno',19,'delete_aluno'),(58,'Can add professor',20,'add_professor'),(59,'Can change professor',20,'change_professor'),(60,'Can delete professor',20,'delete_professor');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_Usuario_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Usuario_id` FOREIGN KEY (`user_id`) REFERENCES `Usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-11-19 21:21:01.452275','1','123456',2,'[{\"changed\": {\"fields\": [\"nome\", \"email\"]}}]',16,1);
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
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'contenttypes','contenttype'),(19,'core','aluno'),(11,'core','arquivosfoto'),(13,'core','arquivosquestao'),(12,'core','arquivosresposta'),(6,'core','candidato'),(7,'core','curso'),(15,'core','disciplina'),(18,'core','disciplinaofertada'),(14,'core','gradecurricular'),(8,'core','periodo'),(20,'core','professor'),(9,'core','questao'),(17,'core','resposta'),(10,'core','turma'),(16,'core','usuario'),(5,'sessions','session');
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
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'core','0001_initial','2017-11-19 21:14:59.199849'),(2,'contenttypes','0001_initial','2017-11-19 21:14:59.231812'),(3,'admin','0001_initial','2017-11-19 21:14:59.309216'),(4,'admin','0002_logentry_remove_auto_add','2017-11-19 21:14:59.330748'),(5,'contenttypes','0002_remove_content_type_name','2017-11-19 21:14:59.413690'),(6,'auth','0001_initial','2017-11-19 21:14:59.606503'),(7,'auth','0002_alter_permission_name_max_length','2017-11-19 21:14:59.629525'),(8,'auth','0003_alter_user_email_max_length','2017-11-19 21:14:59.645052'),(9,'auth','0004_alter_user_username_opts','2017-11-19 21:14:59.662075'),(10,'auth','0005_alter_user_last_login_null','2017-11-19 21:14:59.673736'),(11,'auth','0006_require_contenttypes_0002','2017-11-19 21:14:59.677925'),(12,'auth','0007_alter_validators_add_error_messages','2017-11-19 21:14:59.692326'),(13,'auth','0008_alter_user_username_max_length','2017-11-19 21:14:59.707846'),(14,'sessions','0001_initial','2017-11-19 21:14:59.737747'),(15,'core','0002_auto_20171119_1930','2017-11-19 21:30:30.900273');
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
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('dgn7n7kv0ilo8hub8ugc86gd7qmiz9ks','ZTAwZjJhYmFjYTEyYmI1YjJlYmRlZDA5NTI1YjYzOGU1ZjE0ZDZhOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImQxNzBlNzViZTkzMmE5N2IyZDM0ZGFjYzE2OTczNTRjODNjOGQ2ZTMiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-12-03 21:20:39.898917');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-19 19:32:00


INSERT INTO Usuario (last_login,ra,nome,email,ativo,perfil,password)
VALUES ('2017-11-19 21:20:39.000000',123456,'Admin','admin@handcode.com',1,'C','pbkdf2_sha256$36000$Be2EXve4yCqb$/06J85AYBf6ZOjynsrzyzo65TwxYvOsemDqPx32ceYg=');