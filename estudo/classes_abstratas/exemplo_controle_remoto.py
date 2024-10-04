from abc import ABC, abstractmethod
#importacoes para conseguir criar classes, metodos e properties abstratos

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    #@abstractproperty
    #The class "abstractproperty" is deprecated, Use 'property' with 'abstractmethod' instead
    @abstractmethod
    def marca(self):
        pass
    
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV.")
        
    def desligar(self):
        print("Desligando a TV.")
        
    @property
    def marca(self):
        return 'LG'
        
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o  ar condicionado.")
        
    def desligar(self):
        print("Desligando o  ar condicionado.")
        
    @property
    def marca(self):
        return 'Philco'
        
#classes que implementam uma classe abstrata precisam obrigatoriamente definir 
# o compartamento de cada metodo abstrato


controle= ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle2= ControleArCondicionado()
controle2.ligar()
controle2.desligar()
print(controle2.marca)