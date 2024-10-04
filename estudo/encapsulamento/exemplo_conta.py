class Conta:
    #nao existe encapsulamento em python, apenas uma convenção de utilizar-se 
    #"_" antes do nome da variavel para representar uma variavel privada
    def __init__(self, numAgencia, saldo=0):
        self._saldo=saldo
        self.numAgencia= numAgencia
    
    def depositar(self, valor):
        #devidas verificacoes
        self._saldo += valor 
    
    def sacar(self, valor):
        #devidas verificacoes
        self._saldo -= valor
        
    def mostrarSaldo(self):
        return self._saldo
    
    
conta= Conta('0001',100)
print(conta._saldo) #ainda é possivel acessar diretamente
print(conta.mostrarSaldo())
