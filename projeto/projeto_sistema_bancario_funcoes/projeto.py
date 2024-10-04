import textwrap

def atualizarExtrato(valor, tipo, extrato):
    """_summary_
    Adiciona a descrição da operação que acabou de ser realizada ao extrato
    Args:
        valor (float): valor que foi depositado/sacado
        tipo (char): referente à operação: S-saque, D-deposito
        extrato (string): extrato já existente
    """
    
    if(tipo == 'D'):
        extrato += f'Depósito\t(+)\tR$: {valor:.2f}\n'
    elif(tipo == 'S'):
        extrato += f'Saque\t\t(-)\tR$: {valor:.2f}\n'

    return extrato

def printarExtrato(saldo, / , *, extrato):
    """_summary_
    Printa o extrato da conta
    Args:
        saldo (float): saldo atual
        extrato (string): extrato
    """
    
    print(f'{"="*36}\n\n{"EXTRATO".center(36)}\n\n{"="*36}\n\n')
    print("Sem movimentações" if not extrato else extrato)
    print(f'\nSaldo - R$: {saldo:.2f}\n\n{"="*36}')
    
def sacar(*, saldo, valor, extrato, limite, numeroSaques, limiteSaques):
    if(valor < 0):
        print('[ERRO] Valor inválido para realizar o saque.')

    elif(valor > saldo):
        print('[ERRO] Saldo insuficiente para realizar o saque.')   

    elif(numeroSaques > limiteSaques):
        print('[ERRO] Limite de número saques diário já atingido. Aguarde até amanhã.')

    elif(valor > limite):
        print('[ERRO] O valor excede o limite diário de saques. Aguarde até amanhã.')

    else:
        saldo -= valor
        extrato = atualizarExtrato(valor, 'S', extrato)
        print('[SUCESSO] Valor sacado.')

    return (saldo, extrato)
    
def depositar(saldo, valor, extrato, /):

    if(valor > 0):
        saldo += valor
        extrato = atualizarExtrato(valor, 'D', extrato)
        print('[SUCESSO] Valor depositado.') 
    else:
        print('[ERRO] Valor inválido para realizar o depósito.')

    return saldo, extrato
    
def filtrarUsuario(cpf, usuarios):
    '''caso não haja usuario com o mesmo cpf, a lista criada é vazia'''
    usuariosFiltrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None
    
def criarUsuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario= filtrarUsuario(cpf, usuarios)
    
    if usuario:
        print("[ERRO] Já existe um usuário com esse CPF")
        return
        
    nome = input("Informe o nome completo: ")
    dataNascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({
        "nome": nome,
        "dataNascimento": dataNascimento,
        "cpf": cpf,
        "endereco": endereco        
    })
    
    print("[SUCESSO] Usuário cadastrado com sucesso.")

def criarConta(AGENCIA, numeroConta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario= filtrarUsuario(cpf, usuarios= usuarios)

    if usuario:
        print("[SUCESSO] Conta criada com sucesso.")
        return {
            "agencia": AGENCIA,
            "numeroConta": numeroConta,
            "usuario": usuario
        }
    
    print("[ERRO] Usuário não encontrado")

def listarContas(contas):
    for conta in contas:
        linha = f'''
            Agência:\t{conta['agencia']}
            Nº Conta:\t{conta['numeroConta']}
            Agência:\t{conta['usuario']['nome']}
        '''
        print("="*36)
        print(textwrap.dedent(linha))

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

def main():
    LIMITE_SAQUES=3
    AGENCIA='0001'
    saldo=0
    limite= 1500
    extrato=''
    numeroSaques=0
    usuarios=[]
    contas=[]

    while True:
        op = menu()
        
        if(op == 'D'):
            valor=float(input("Valor do depósito => R$: "))

            saldo, extrato = depositar(saldo, valor, extrato)
            
            continue
        
        elif(op == 'S'):
            valor=float(input("Valor do saque => R$: "))
            
            saldo, extrato= sacar(
                saldo= saldo, 
                valor= valor, 
                extrato= extrato, 
                limite= limite, 
                numeroSaques= numeroSaques, 
                limiteSaques= LIMITE_SAQUES
            )
            if(valor>0 and valor<=limite and numeroSaques<=LIMITE_SAQUES):
                limite -= valor
                numeroSaques += 1
                
            continue
        
        elif(op == 'E'):
            
            printarExtrato(saldo , extrato=extrato)
                
            continue
        
        elif(op == 'NU'):
            criarUsuario(usuarios)
            
            continue
        
        elif(op == 'NC'):
            numeroConta = len(contas) + 1
            conta= criarConta(AGENCIA, numeroConta, usuarios)
            
            if conta:
                contas.append(conta)
            
            continue
        
        elif(op == 'LC'):
            listarContas(contas)
            
            continue
        
        elif(op == 'Q'):
            
            break
        
        else:
            print('Operação inválida, por favor selecione novamente.')
            
main()


