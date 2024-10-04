class Pessoa:
    def __init__(self, nome= None, idade= None):
        self.nome= nome
        self.idade= idade
        
    @classmethod
    def criar_de_data_nascimento(cls, ano, nome):
        idade= 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18
    
p= Pessoa.criar_de_data_nascimento(2004, 'Otto')
print(p.nome, p.idade)

print(Pessoa.e_maior_de_idade(16))
print(Pessoa.e_maior_de_idade(27))