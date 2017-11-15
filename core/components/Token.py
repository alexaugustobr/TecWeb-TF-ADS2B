
class Token:
    idAluno = None
    idTurma = None
    dataCriacao = None


    def __init__(self,idAluno,idTurma,dataCriacao):
        self.idAluno = idAluno
        self.idTurma = idTurma
        self.dataCriacao = dataCriacao

    def __str__(self):
        return "{}.{}.{}".format(self.idAluno,self.idTurma,self.dataCriacao)
