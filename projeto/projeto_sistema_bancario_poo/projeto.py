from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

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
        return self._agencia
    
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
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })

def printarExtrato(clientes):   
    cpf= input("Informe o cpf do cliente (somente numeros) => ")
    cliente= filtrarCliente(cpf, clientes)
    
    if not cliente:
        print('[ERRO] Cliente nao encontrado.')
        return 
    
    conta= recuperarContaCliente(cliente)
    
    if not conta:
        return
    
    print(f'{"="*36}\n\n{"EXTRATO".center(36)}\n\n{"="*36}\n')
    transacoes= conta.historico.transacoes
    
    extrato=''
    if not transacoes:
        extrato="Não foram realizadas transações."
    else:
        for transacao in transacoes:
            extrato+= f"\n{transacao['tipo']}:\n\tR$: {transacao['valor']:.2f}\n"
    
    print(extrato)
    print(f'Saldo:\n\tR$: {conta.saldo:.2f}\n\n{"="*36}')


#corrigir (post no forum aguardando resposta)
def realizarOperacao(clientes, operacao):
    cpf= input("Informe o cpf do cliente (somente numeros) => ")
    cliente= filtrarCliente(cpf, clientes)
    
    if not cliente:
        print('[ERRO] Cliente nao encontrado.')
        return 
    
    valor= float(input(f"Informe o valor do {operacao.__class__.__name__} => R$: "))
    transacao= operacao(valor)
    
    conta= recuperarContaCliente(cliente)
    
    if not conta:
        return
    
    cliente.realizarTransacao(conta, transacao)
    
  
def filtrarCliente(cpf, clientes):
    #caso não haja usuario com o mesmo cpf, a lista criada é vazia
    clientesFiltrados = [cliente                    #retorno
                         for cliente in clientes    #iteracao
                         if cliente.cpf == cpf]     #condicao
    
    return clientesFiltrados[0] if clientesFiltrados else None
    
def recuperarContaCliente(cliente):
    if not cliente.contas:
        print("[ERRO] Cliente não possui uma conta.")
        return
    
    #ainda nao permite o cliente escolher qual das contas realizar as operacoes
    return cliente.contas[0]

def criarCliente(clientes):
    cpf = input("Informe o CPF (somente numeros): ")
    cliente= filtrarCliente(cpf, clientes)
    
    if cliente:
        print("[ERRO] Já existe um cliente com esse CPF")
        return
        
    nome = input("Informe o nome completo: ")
    dataNascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    cliente= PessoaFisica(nome= nome, dataNascimento= dataNascimento, cpf= cpf, endereco= endereco)
    
    clientes.append(cliente)
    
    print("[SUCESSO] Usuário cadastrado com sucesso.")

def criarConta(numeroConta, clientes, contas):
    cpf= input("Informe o cpf do cliente (somente numeros) => ")
    cliente= filtrarCliente(cpf, clientes)

    if cliente:
        conta= ContaCorrente.novaConta(cliente= cliente, numero= numeroConta)
        contas.append(conta)
        cliente.contas.append(conta)
        
        print("[SUCESSO] Conta criada com sucesso.")
        return
    
    print("[ERRO] Usuário não encontrado")

def listarContas(contas):
    for conta in contas:
        print("="*36)
        print(textwrap.dedent(str(conta)))

def menu():
    menu="""\n
    =============== MENU ===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair  
    => """
    return input(textwrap.dedent(menu)).upper()

def sacar(clientes):
    cpf= input("Informe o cpf do cliente (somente numeros) => ")
    cliente= filtrarCliente(cpf, clientes)
    
    if not cliente:
        print('[ERRO] Cliente nao encontrado.')
        return 
    
    valor= float(input("Informe o valor do saque => R$: "))
    transacao= Saque(valor)
    
    conta= recuperarContaCliente(cliente)
    
    if not conta:
        return
    
    cliente.realizarTransacao(conta, transacao)
    
def depositar(clientes):
    cpf= input("Informe o cpf do cliente (somente numeros) => ")
    cliente= filtrarCliente(cpf, clientes)
    
    if not cliente:
        print('[ERRO] Cliente nao encontrado.')
        return 
    
    valor= float(input("Informe o valor do deposito => R$: "))
    transacao= Deposito(valor)
    
    conta= recuperarContaCliente(cliente)
    
    if not conta:
        return
    
    cliente.realizarTransacao(conta, transacao)

def main():
    clientes= []
    contas= []

    while True:
        op = menu()
        
        if(op == 'D'):
            #realizarOperacao(clientes, Deposito)
            depositar(clientes)
            
        elif(op == 'S'):
            #realizarOperacao(clientes, Saque)
            sacar(clientes)
            
        elif(op == 'E'):
            printarExtrato(clientes)
        
        elif(op == 'NU'):
            criarCliente(clientes)
        
        elif(op == 'NC'):
            numeroConta = len(contas) + 1
            criarConta(numeroConta, clientes, contas)
        
        elif(op == 'LC'):
            listarContas(contas)
        
        elif(op == 'Q'):
            break
        
        else:
            print('Operação inválida, por favor selecione novamente.')
            
main()