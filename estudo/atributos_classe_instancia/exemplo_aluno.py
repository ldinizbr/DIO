class Aluno:
    escola='DIO'        #variavel de classe
    
    def __init__(self, nome, matricula): #variaveis de instancia
        self.nome= nome
        self.matricula= matricula
    
    def __str__(self) -> str:
        return f'{self.nome} ({self.matricula}) - {self.escola}'
    
al1= Aluno('Otto', 1231)
al2= Aluno('Jose', 3512)

print(al1)
print(al2)

Aluno.escola = 'python'
al1.matricula= 1

al3= Aluno('Claudio', 3)

print(al1)
print(al2)
print(al3)

#self = instancia