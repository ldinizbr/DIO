from abc import ABC, abstractmethod
import datetime

class Conta:    
    def __init__(self, cliente, numero):
        self._cliente= cliente
        self._numero= numero
        self._saldo= 0
        self._agencia= agencia='0001'
        self._historico= Historico()
    
    @classmethod
    def novaConta(cls, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def depositar(self, valor):
        if(valor > 0):
            self._saldo += valor
            print("[SUCESSO] Operação realizada.")
            return True
        
        else:
            print("[ERRO] Valor inválido.")
            
        return False
         
    def sacar(self, valor):
        saldo= self.saldo
        
        if(valor > saldo):
            print("[ERRO] Saldo insuficiente")
            
        elif(valor > 0):
            self._saldo -= valor
            print("[SUCESSO] Operação realizada.")
            return True
        
        else:
            print("[ERRO] Valor inválido.")
            
        return False
           
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite= 1000, limiteSaques=3):
        self.limite= limite
        self.limiteSaques= limiteSaques
        super().__init__(cliente, numero)
        
    #override
    def sacar(self, valor):
        #conta quantas transacoes existem do tipo saque
        numeroSaques= len( [transacao for transacao in self.historico.transacoes
                            if transacao["tipo"] == Saque.__name__])
        
        if(valor > self.limite):
            print("[ERRO] Valor a se sacar excede o limite.")
        elif(numeroSaques >= self.limiteSaques):
            print("[ERRO] Limite máximo de saques atingido")
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f'''\
            Agencia:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            '''

class Cliente:
    def __init__(self, endereco):
        self.endereco= endereco
        self.contas= []
        
    def realizarTransacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionarConta(self, conta):
        self.contas.append(conta)
    
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, dataNascimento):
        super().__init__(endereco)
        self.nome= nome
        self.cpf= cpf
        self.dataNascimento= dataNascimento
        
class Transcao(ABC):
    @abstractmethod
    def registrar(conta):
        pass
    
    @property
    @abstractmethod
    def valor(self):
        pass

class Saque(Transcao):
    def __init__(self, valor):
        self._valor= valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if(conta.sacar(self.valor)):
            conta.historico.adicionarTransacao(self)
    
class Deposito(Transcao):
    def __init__(self, valor):
        self._valor= valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if(conta.depositar(self.valor)):
            conta.historico.adicionarTransacao(self)
     
class Historico:
    def __init__(self):
        self._transacoes= []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionarTransacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
        })
    