
USE localdb;

DROP TABLE IF EXISTS Aluno;
CREATE TABLE Aluno (
  usuario_ptr_id int(11) NOT NULL,
  celular varchar(11) DEFAULT NULL,
  curso_id int(11) NOT NULL,
  foto_id int(11) DEFAULT NULL,
  PRIMARY KEY (usuario_ptr_id),
  KEY FK_ALUNO_CURSO (curso_id),
  KEY FK_ALUNO_ARQUIVOS_FOTO (foto_id),
  CONSTRAINT FK_ALUNO_CURSO FOREIGN KEY (curso_id) REFERENCES Curso (id),
  CONSTRAINT FK_ALUNO_ARQUIVOS_FOTO FOREIGN KEY (foto_id) REFERENCES ArquivosFoto (id),
  CONSTRAINT FF_ALUNO_USUARIO_ID FOREIGN KEY (usuario_ptr_id) REFERENCES Usuario (id)
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
  KEY FK_ARQUIVOS_QUESTAO_QUESTAO_ID (questao_id),
  CONSTRAINT FK_ARQUIVOS_QUESTAO_QUESTAO_ID FOREIGN KEY (questao_id) REFERENCES Questao (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE ArquivosResposta (
  id int(11) NOT NULL AUTO_INCREMENT,
  arquivo varchar(500) NOT NULL,
  resposta_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY FK_ARQUIVOS_RESPOSTA_RESPOSTA_ID (resposta_id),
  CONSTRAINT FK_ARQUIVOS_RESPOSTA_RESPOSTA_ID FOREIGN KEY (resposta_id) REFERENCES Resposta (id)
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
  KEY FK_CANDIDATO_ARQUIVOS_FOTO (foto_id),
  KEY FK_CANDIDATO_TURMA_ID (turma_id),
  KEY FK_CANDIDATO_ALUNO_USUARIO_ID (aluno_id),
  CONSTRAINT FK_CANDIDATO_ALUNO_USUARIO_ID FOREIGN KEY (aluno_id) REFERENCES Aluno (usuario_ptr_id),
  CONSTRAINT FK_CANDIDATO_ARQUIVOS_FOTO FOREIGN KEY (foto_id) REFERENCES ArquivosFoto (id),
  CONSTRAINT FK_CANDIDATO_TURMA_ID FOREIGN KEY (turma_id) REFERENCES Turma (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
  UNIQUE KEY UN_TURMA_CURSO_ID (turma_id,curso_id),
  KEY FK_CURSO_TURMA_CURSO (curso_id),
  CONSTRAINT FK_CURSO_TURMA_CURSO FOREIGN KEY (curso_id) REFERENCES Curso (id),
  CONSTRAINT FK_CURSO_TURMA_TURMA_ID FOREIGN KEY (turma_id) REFERENCES Turma (id)
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
  KEY FK_DISCIPLINA_OFERTADA_DISCIPLINA_ID (disciplina_id),
  CONSTRAINT FK_DISCIPLINA_OFERTADA_DISCIPLINA_ID FOREIGN KEY (disciplina_id) REFERENCES Disciplina (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE GradeCurricular (
  id int(11) NOT NULL AUTO_INCREMENT,
  ano smallint(6) NOT NULL,
  semestre varchar(1) NOT NULL,
  curso_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY FK_GRADE_CURRICULAR_CURSO_ID (curso_id),
  CONSTRAINT FK_GRADE_CURRICULAR_CURSO_ID FOREIGN KEY (curso_id) REFERENCES Curso (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Matricula (
  id int(11) NOT NULL AUTO_INCREMENT,
  aluno_id int(11) NOT NULL,
  turma_id int(11) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY UN_TURMA_ALUNO (aluno_id,turma_id),
  KEY FK_MATRICULA_ID (turma_id),
  CONSTRAINT FK_MATRICULA_USUARIO_ID FOREIGN KEY (aluno_id) REFERENCES Aluno (usuario_ptr_id),
  CONSTRAINT FK_MATRICULA_ID FOREIGN KEY (turma_id) REFERENCES Turma (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Periodo (
  id int(11) NOT NULL AUTO_INCREMENT,
  numero smallint(6) NOT NULL,
  gradeCurricular_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY FK_PERIODO_GRADE_CURRICULAR (gradeCurricular_id),
  CONSTRAINT FK_PERIODO_GRADE_CURRICULAR FOREIGN KEY (gradeCurricular_id) REFERENCES GradeCurricular (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE PeriodoDisicplina (
  id int(11) NOT NULL AUTO_INCREMENT,
  periodo_id int(11) NOT NULL,
  disciplina_id int(11) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY PeriodoDisicplina_periodo_id_disciplina_id_4d696e73_uniq (periodo_id,disciplina_id),
  KEY FK_PERIODO_DISCIPLINA_DISICPLINA (disciplina_id),
  CONSTRAINT FK_PERIODO_DISCIPLINA_DISICPLINA FOREIGN KEY (disciplina_id) REFERENCES Disciplina (id),
  CONSTRAINT FK_PERIODO_DISCIPLINA_PERIODO FOREIGN KEY (periodo_id) REFERENCES Periodo (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Professor (
  usuario_ptr_id int(11) NOT NULL,
  apelido varchar(30) DEFAULT NULL,
  celular varchar(11) NOT NULL,
  PRIMARY KEY (usuario_ptr_id),
  UNIQUE KEY apelido (apelido),
  CONSTRAINT FK_PROFESSOR_USUARIO FOREIGN KEY (usuario_ptr_id) REFERENCES Usuario (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Questao (
  id int(11) NOT NULL AUTO_INCREMENT,
  descricao longtext NOT NULL,
  data_limite_entrega date NOT NULL,
  numero int(11) NOT NULL,
  data date NOT NULL,
  turma_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY FK_QUESTAO_TURMA (turma_id),
  CONSTRAINT FK_QUESTAO_TURMA FOREIGN KEY (turma_id) REFERENCES Turma (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Resposta (
  id int(11) NOT NULL AUTO_INCREMENT,
  data_avaliacao date DEFAULT NULL,
  nota decimal(4,2) DEFAULT NULL,
  avaliacao longtext,
  descricao longtext NOT NULL,
  data_de_envio date NOT NULL,
  questao_id int(11) NOT NULL,
  aluno_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY FK_RESPOSTA_QUESTAO (questao_id),
  KEY FK_RESPOSTA_ALUNO (aluno_id),
  CONSTRAINT FK_RESPOSTA_ALUNO FOREIGN KEY (aluno_id) REFERENCES Aluno (usuario_ptr_id),
  CONSTRAINT FK_RESPOSTA_QUESTAO FOREIGN KEY (questao_id) REFERENCES Questao (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Turma (
  id int(11) NOT NULL AUTO_INCREMENT,
  turno varchar(15) NOT NULL,
  turma_sigla varchar(1) NOT NULL,
  disciplinaOfertada_id int(11) NOT NULL,
  professor_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY FK_TURMA_DISCIPLINA_OFERTADA (disciplinaOfertada_id),
  KEY FK_TURMA_PROFESSOR_USUARIO (professor_id),
  CONSTRAINT FK_TURMA_DISCIPLINA_OFERTADA FOREIGN KEY (disciplinaOfertada_id) REFERENCES DisciplinaOfertada (id),
  CONSTRAINT FK_TURMA_PROFESSOR_USUARIO FOREIGN KEY (professor_id) REFERENCES Professor (usuario_ptr_id)
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;