
class Token:
    idAluno = None
    idTurma = None
    segundos = None


    def __init__(self,idAluno,idTurma,segundos):
        self.idAluno = idAluno
        self.idTurma = idTurma
        self.segundos = segundos

    def __str__(self):
        return "{}.{}.{}".format(self.idAluno,self.idTurma,self.segundos)
