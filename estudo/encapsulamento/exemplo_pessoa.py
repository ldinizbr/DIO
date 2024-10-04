class Pessoa:
    def __init__(self, nome, anoNascimeto):
        self._nome= nome
        self._anoNascimento= anoNascimeto
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        anoAtual=2024
        return anoAtual - self._anoNascimento   #exemplo
    
pessoa= Pessoa("Otto", 2004)

print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

#é possível utilizar-se de getters e setters igual em Java e C++
#porém, utiliza-se o @property, por ser mais conveniente ao Python