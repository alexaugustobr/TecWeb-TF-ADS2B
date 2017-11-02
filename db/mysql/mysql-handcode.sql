
CREATE DATABASE handcode;

USE handcode;


CREATE TABLE Disciplina (
    nome VARCHAR(150) NOT NULL,
    carga_horaria TINYINT(4),
    teoria DECIMAL(3 , 0 ),
    pratica DECIMAL(3 , 0 ),
    ementa TEXT,
    competencias TEXT,
    habilidades TEXT,
    conteudo TEXT,
    bibliografia_basica TEXT,
    bibliografia_complementar TEXT,
    PRIMARY KEY (nome)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Professor (
    ra INT(11) NOT NULL,
    apelido VARCHAR(30),
    nome VARCHAR(120),
    celular VARCHAR(11),
    email VARCHAR(80),
    PRIMARY KEY (ra),
    UNIQUE KEY UNIQUE_professor_apelido (apelido)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE DisciplinaOfertada (
    nome_disciplina VARCHAR(240) NOT NULL,
    ano SMALLINT NOT NULL,
    semestre CHAR(1) NOT NULL,
    PRIMARY KEY (nome_disciplina , ano, semestre),
    CONSTRAINT fk_disciplina_ofertada_disciplina FOREIGN KEY (nome_disciplina)
        REFERENCES Disciplina (nome)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Curso (
    sigla VARCHAR(5) NOT NULL,
    nome VARCHAR(50),
    PRIMARY KEY (sigla),
    UNIQUE KEY UNIQUE_curso_nome (nome)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE GradeCurricular(
    sigla_curso VARCHAR(5) NOT NULL,
    ano SMALLINT NOT NULL,
    semestre CHAR(1) NOT NULL,
    PRIMARY KEY (sigla_curso, ano, semestre),
    CONSTRAINT fk_GradeCurricular_curso FOREIGN KEY (sigla_curso)
        REFERENCES Curso (sigla)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Periodo (
    sigla_curso VARCHAR(5) NOT NULL,
    ano_grade SMALLINT NOT NULL,
    semestre_grade CHAR(1) NOT NULL,
    numero TINYINT NOT NULL,
    PRIMARY KEY (sigla_curso, ano_grade, semestre_grade, numero),
    CONSTRAINT fk_periodo_gradecurricular
    FOREIGN KEY (sigla_curso,ano_grade,semestre_grade)
        REFERENCES GradeCurricular (sigla_curso,ano,semestre)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE PeriodoDisciplina (
    sigla_curso VARCHAR(5) NOT NULL,
    ano_grade SMALLINT NOT NULL,
    semestre_grade CHAR(1) NOT NULL,
    numero_periodo TINYINT NOT NULL,
    nome_disciplina VARCHAR(240) NOT NULL,
    PRIMARY KEY (sigla_curso , ano_grade , semestre_grade , nome_disciplina , numero_periodo),
    CONSTRAINT fk_periododisciplina_periodo 
    FOREIGN KEY (sigla_curso , ano_grade , semestre_grade , numero_periodo)
        REFERENCES Periodo (sigla_curso , ano_grade , semestre_grade , numero),
    FOREIGN KEY (nome_disciplina)
        REFERENCES Disciplina (nome)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE Turma (
    nome_disciplina VARCHAR(240) NOT NULL,
    ano_ofertado SMALLINT NOT NULL,
    semestre_ofertado CHAR(1) NOT NULL,
    id CHAR(1) NOT NULL,
    turno VARCHAR(15),
    ra_professor int(11),
    PRIMARY KEY (nome_disciplina,ano_ofertado,semestre_ofertado, id),
    CONSTRAINT fk_turma_professor
    FOREIGN KEY (ra_professor) 
        REFERENCES Professor (ra),
    CONSTRAINT fk_turma_disciplinaofertada 
    FOREIGN KEY (nome_disciplina, ano_ofertado, semestre_ofertado)
        REFERENCES DisciplinaOfertada (nome_disciplina,  ano, semestre)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Questao (
    nome_disciplina VARCHAR(240) NOT NULL,
    ano_ofertado SMALLINT NOT NULL,
    semestre_ofertado CHAR(1) NOT NULL,
    id_turma CHAR(1) NOT NULL,
    numero INT(11) NOT NULL,
    data_limite_entrega DATE,
    descricao TEXT,
    data DATE,
    PRIMARY KEY (nome_disciplina,ano_ofertado,semestre_ofertado,id_turma,numero),  
    CONSTRAINT fk_questao_turma  
    FOREIGN KEY (nome_disciplina, ano_ofertado,semestre_ofertado,id_turma)  
        REFERENCES Turma (nome_disciplina,ano_ofertado,semestre_ofertado,id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE ArquivoResposta (
    nome_disciplina VARCHAR(240) NOT NULL,
    ano_ofertado SMALLINT NOT NULL,
    semestre_ofertado CHAR(1) NOT NULL,
    id_turma CHAR(1) NOT NULL,
    arquivo VARCHAR(500) NOT NULL,
    PRIMARY KEY (nome_disciplina,ano_ofertado,semestre_ofertado,id_turma,arquivo),  
    CONSTRAINT fk_arquivo_questao
    FOREIGN KEY (nome_disciplina, ano_ofertado,semestre_ofertado,id_turma)  
        REFERENCES Questao (nome_disciplina,ano_ofertado,semestre_ofertado,id_turma)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Aluno (
    ra INT(11) NOT NULL,
    nome VARCHAR(120),
    email VARCHAR(80),
    celular CHAR(11),
    sigla_curso CHAR(5) NOT NULL,
    PRIMARY KEY (ra),
    CONSTRAINT fk_aluno_curso FOREIGN KEY (sigla_curso)
        REFERENCES Curso (sigla)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Matricula (
    ra_aluno INT(11) NOT NULL,
    nome_disciplina VARCHAR(240) NOT NULL,
    ano_ofertado SMALLINT NOT NULL,
    semestre_ofertado CHAR(1) NOT NULL,
    id_turma CHAR(1) NOT NULL,
    PRIMARY KEY (ra_aluno,nome_disciplina,ano_ofertado,semestre_ofertado,id_turma),  
    CONSTRAINT fk_matricula_turma
    FOREIGN KEY (nome_disciplina, ano_ofertado,semestre_ofertado,id_turma)  
        REFERENCES Turma (nome_disciplina,ano_ofertado,semestre_ofertado,id),
    CONSTRAINT fk_matricula_aluno
    FOREIGN KEY (ra_aluno)  
        REFERENCES Aluno (ra)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
