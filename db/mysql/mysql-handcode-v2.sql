CREATE DATABASE HANDCODE;

USE HANDCODE;

CREATE TABLE Aluno (
  usuario_ptr_id int(11) NOT NULL,
  celular varchar(11) DEFAULT NULL,
  curso_id int(11) NOT NULL,
  foto_id int(11) DEFAULT NULL,
  PRIMARY KEY (usuario_ptr_id),
  KEY Aluno_curso_id_74ab1773_fk_Curso_id (curso_id),
  KEY Aluno_foto_id_4ad2beec_fk_ArquivosFoto_id (foto_id),
  CONSTRAINT Aluno_curso_id_74ab1773_fk_Curso_id FOREIGN KEY (curso_id) REFERENCES Curso (id),
  CONSTRAINT Aluno_foto_id_4ad2beec_fk_ArquivosFoto_id FOREIGN KEY (foto_id) REFERENCES ArquivosFoto (id),
  CONSTRAINT Aluno_usuario_ptr_id_11d10b0e_fk_Usuario_id FOREIGN KEY (usuario_ptr_id) REFERENCES Usuario (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE ArquivosFoto (
  id int(11) NOT NULL AUTO_INCREMENT,
  arquivo varchar(10000) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE ArquivosQuestao (
  id int(11) NOT NULL AUTO_INCREMENT,
  arquivo varchar(500) NOT NULL,
  questao_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY ArquivosQuestao_questao_id_39754589_fk_Questao_id (questao_id),
  CONSTRAINT ArquivosQuestao_questao_id_39754589_fk_Questao_id FOREIGN KEY (questao_id) REFERENCES Questao (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE ArquivosResposta (
  id int(11) NOT NULL AUTO_INCREMENT,
  arquivo varchar(500) NOT NULL,
  resposta_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY ArquivosResposta_resposta_id_f2b8a662_fk_Resposta_id (resposta_id),
  CONSTRAINT ArquivosResposta_resposta_id_f2b8a662_fk_Resposta_id FOREIGN KEY (resposta_id) REFERENCES Resposta (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Candidado (
  id int(11) NOT NULL AUTO_INCREMENT,
  nome varchar(120) DEFAULT NULL,
  ra varchar(80) DEFAULT NULL,
  email varchar(80) DEFAULT NULL,
  celular varchar(11) DEFAULT NULL,
  codigo_acesso varchar(120) DEFAULT NULL,
  matricula_aceita tinyint(1) NOT NULL,
  confirmado tinyint(1) NOT NULL,
  foto_id int(11) DEFAULT NULL,
  turma_id int(11) DEFAULT NULL,
  aluno_id int(11) DEFAULT NULL,
  PRIMARY KEY (id),
  KEY Candidado_foto_id_96c02125_fk_ArquivosFoto_id (foto_id),
  KEY Candidado_turma_id_5befcac3_fk_Turma_id (turma_id),
  KEY Candidado_aluno_id_506fe92f_fk_Aluno_usuario_ptr_id (aluno_id),
  CONSTRAINT Candidado_aluno_id_506fe92f_fk_Aluno_usuario_ptr_id FOREIGN KEY (aluno_id) REFERENCES Aluno (usuario_ptr_id),
  CONSTRAINT Candidado_foto_id_96c02125_fk_ArquivosFoto_id FOREIGN KEY (foto_id) REFERENCES ArquivosFoto (id),
  CONSTRAINT Candidado_turma_id_5befcac3_fk_Turma_id FOREIGN KEY (turma_id) REFERENCES Turma (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS Curso;

CREATE TABLE Curso (
  id int(11) NOT NULL AUTO_INCREMENT,
  sigla varchar(5) NOT NULL,
  nome varchar(50) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY sigla (sigla),
  UNIQUE KEY nome (nome)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE CursoTurma (
  id int(11) NOT NULL AUTO_INCREMENT,
  turma_id int(11) NOT NULL,
  curso_id int(11) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY CursoTurma_turma_id_curso_id_7723c433_uniq (turma_id,curso_id),
  KEY CursoTurma_curso_id_aee9d168_fk_Curso_id (curso_id),
  CONSTRAINT CursoTurma_curso_id_aee9d168_fk_Curso_id FOREIGN KEY (curso_id) REFERENCES Curso (id),
  CONSTRAINT CursoTurma_turma_id_12eaad28_fk_Turma_id FOREIGN KEY (turma_id) REFERENCES Turma (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Disciplina (
  id int(11) NOT NULL AUTO_INCREMENT,
  nome varchar(240) NOT NULL,
  carga_horaria smallint(6) NOT NULL,
  teoria decimal(3,2) NOT NULL,
  pratica decimal(3,2) NOT NULL,
  ementa longtext NOT NULL,
  competencias longtext NOT NULL,
  habilidades longtext NOT NULL,
  conteudo longtext NOT NULL,
  bibliografia_complementar longtext NOT NULL,
  bibliografia_basica longtext NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE DisciplinaOfertada (
  id int(11) NOT NULL AUTO_INCREMENT,
  ano smallint(6) NOT NULL,
  semestre varchar(1) NOT NULL,
  disciplina_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY DisciplinaOfertada_disciplina_id_0d7cb697_fk_Disciplina_id (disciplina_id),
  CONSTRAINT DisciplinaOfertada_disciplina_id_0d7cb697_fk_Disciplina_id FOREIGN KEY (disciplina_id) REFERENCES Disciplina (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE GradeCurricular (
  id int(11) NOT NULL AUTO_INCREMENT,
  ano smallint(6) NOT NULL,
  semestre varchar(1) NOT NULL,
  curso_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY GradeCurricular_curso_id_92730f1c_fk_Curso_id (curso_id),
  CONSTRAINT GradeCurricular_curso_id_92730f1c_fk_Curso_id FOREIGN KEY (curso_id) REFERENCES Curso (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE Matricula (
  id int(11) NOT NULL AUTO_INCREMENT,
  aluno_id int(11) NOT NULL,
  turma_id int(11) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY Matricula_aluno_id_turma_id_460cd5b1_uniq (aluno_id,turma_id),
  KEY Matricula_turma_id_262a5d60_fk_Turma_id (turma_id),
  CONSTRAINT Matricula_aluno_id_ef0199a0_fk_Aluno_usuario_ptr_id FOREIGN KEY (aluno_id) REFERENCES Aluno (usuario_ptr_id),
  CONSTRAINT Matricula_turma_id_262a5d60_fk_Turma_id FOREIGN KEY (turma_id) REFERENCES Turma (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Periodo (
  id int(11) NOT NULL AUTO_INCREMENT,
  numero smallint(6) NOT NULL,
  gradeCurricular_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY Periodo_gradeCurricular_id_e07688d0_fk_GradeCurricular_id (gradeCurricular_id),
  CONSTRAINT Periodo_gradeCurricular_id_e07688d0_fk_GradeCurricular_id FOREIGN KEY (gradeCurricular_id) REFERENCES GradeCurricular (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE PeriodoDisicplina (
  id int(11) NOT NULL AUTO_INCREMENT,
  periodo_id int(11) NOT NULL,
  disciplina_id int(11) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY PeriodoDisicplina_periodo_id_disciplina_id_4d696e73_uniq (periodo_id,disciplina_id),
  KEY PeriodoDisicplina_disciplina_id_4fd67309_fk_Disciplina_id (disciplina_id),
  CONSTRAINT PeriodoDisicplina_disciplina_id_4fd67309_fk_Disciplina_id FOREIGN KEY (disciplina_id) REFERENCES Disciplina (id),
  CONSTRAINT PeriodoDisicplina_periodo_id_54aa0b41_fk_Periodo_id FOREIGN KEY (periodo_id) REFERENCES Periodo (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Professor (
  usuario_ptr_id int(11) NOT NULL,
  apelido varchar(30) DEFAULT NULL,
  celular varchar(11) NOT NULL,
  PRIMARY KEY (usuario_ptr_id),
  UNIQUE KEY apelido (apelido),
  CONSTRAINT Professor_usuario_ptr_id_d7315225_fk_Usuario_id FOREIGN KEY (usuario_ptr_id) REFERENCES Usuario (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Questao (
  id int(11) NOT NULL AUTO_INCREMENT,
  descricao longtext NOT NULL,
  data_limite_entrega date NOT NULL,
  numero int(11) NOT NULL,
  data date NOT NULL,
  turma_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY Questao_turma_id_2697c4b4_fk_Turma_id (turma_id),
  CONSTRAINT Questao_turma_id_2697c4b4_fk_Turma_id FOREIGN KEY (turma_id) REFERENCES Turma (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Resposta (
  id int(11) NOT NULL AUTO_INCREMENT,
  data_avaliacao date NOT NULL,
  nota decimal(4,2) NOT NULL,
  avaliacao longtext NOT NULL,
  descricao longtext NOT NULL,
  data_de_envio date NOT NULL,
  questao_id int(11) NOT NULL,
  aluno_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY Resposta_questao_id_85f566c5_fk_Questao_id (questao_id),
  KEY Resposta_aluno_id_0279393c_fk_Aluno_usuario_ptr_id (aluno_id),
  CONSTRAINT Resposta_aluno_id_0279393c_fk_Aluno_usuario_ptr_id FOREIGN KEY (aluno_id) REFERENCES Aluno (usuario_ptr_id),
  CONSTRAINT Resposta_questao_id_85f566c5_fk_Questao_id FOREIGN KEY (questao_id) REFERENCES Questao (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Turma (
  id int(11) NOT NULL AUTO_INCREMENT,
  turno varchar(15) NOT NULL,
  turma_sigla varchar(1) NOT NULL,
  disciplinaOfertada_id int(11) NOT NULL,
  professor_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY Turma_disciplinaOfertada_id_df16d165_fk_DisciplinaOfertada_id (disciplinaOfertada_id),
  KEY Turma_professor_id_9202676b_fk_Professor_usuario_ptr_id (professor_id),
  CONSTRAINT Turma_disciplinaOfertada_id_df16d165_fk_DisciplinaOfertada_id FOREIGN KEY (disciplinaOfertada_id) REFERENCES DisciplinaOfertada (id),
  CONSTRAINT Turma_professor_id_9202676b_fk_Professor_usuario_ptr_id FOREIGN KEY (professor_id) REFERENCES Professor (usuario_ptr_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Usuario (
  id int(11) NOT NULL AUTO_INCREMENT,
  last_login datetime(6) DEFAULT NULL,
  ra int(11) NOT NULL,
  nome varchar(100) NOT NULL,
  email varchar(254) NOT NULL,
  ativo tinyint(1) NOT NULL,
  perfil varchar(1) NOT NULL,
  password varchar(150) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY ra (ra),
  UNIQUE KEY email (email)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO Usuario (id,last_login,ra,nome,email,ativo,perfil,password)
VALUES ('2017-11-19 21:20:39.000000',123456,'Admin','admin@handcode.com',1,'C','pbkdf2_sha256$36000$Be2EXve4yCqb$/06J85AYBf6ZOjynsrzyzo65TwxYvOsemDqPx32ceYg=');