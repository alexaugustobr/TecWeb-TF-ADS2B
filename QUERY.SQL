1 - 
SELECT USUARIO.NOME, USUARIO.EMAIL, USUARIO.RA FROM ALUNO
INNER JOIN USUARIO
ON ALUNO.usuario_ptr_id = USUARIO.ID
INNER JOIN CURSO
ON ALUNO.curso_id = CURSO.ID
WHERE CURSO.sigla = 'ADS'
2 -
SELECT DISCIPLINA.NOME FROM DISCIPLINAOFERTADA
INNER JOIN DISCIPLINA
ON DISCIPLINA.id = DISCIPLINAOFERTADA.id
INNER JOIN TURMA
ON TURMA.disciplinaOfertada_id = DISCIPLINAOFERTADA.ID
INNER JOIN CURSOTURMA
ON CURSOTURMA.turma_id = TURMA.ID
INNER JOIN CURSO
ON CURSO.id = CURSOTURMA.turma_id
WHERE ANO = 2018 AND CURSO.sigla = 'ADS'
3-
select questao.* from questao 
left join resposta
on questao.id = resposta.questao_id
where questao.id not in
    (select questao_id from resposta 
    inner join aluno 
    on aluno.usuario_ptr_id = resposta.aluno_id 
    where aluno.usuario_ptr_id = 5)

4-
SELECT * FROM ALUNO 
LEFT JOIN MATRICULA 
ON aluno.usuario_ptr_id = MATRICULA.ALUNO_ID
LEFT JOIN TURMA
ON turma.id = MATRICULA.turma_id
LEFT JOIN DisciplinaOfertada
ON DisciplinaOfertada.id = TURMA.disciplinaOfertada_id
WHERE disciplinaOfertada_id NOT IN (SELECT disciplinaOfertada_id FROM TURMA WHERE TURMA.ID = 2) OR disciplinaOfertada_id IS NULL