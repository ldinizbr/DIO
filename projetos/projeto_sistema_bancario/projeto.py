def adicionarExtrato(valor, tipo):
    """_summary_
    Adiciona a descrição da operação que acabou de ser realizada ao extrato
    Args:
        valor (float): valor que foi depositado/sacado
        tipo (char): referente à operação: S-saque, D-deposito
    """
    
    global extrato
    global numero_operacoes
    numero_operacoes += 1
    if(tipo == 'D'):
        extrato += f'{numero_operacoes} - Depósito (+) R$: {valor:.2f}\n'
    elif(tipo == 'S'):
        extrato += f'{numero_operacoes} - Saque (-) R$: {valor:.2f}\n'

def printarExtrato(saldo = 0):
    """_summary_
    Printa o extrato da conta - cabecalho + extrato + saldo + rodape
    Args:
        saldo (float): saldo atual
    """
    
    cabecalho = f'{"="*30}\n\n{"EXTRATO".center(30)}\n\n{"="*30}\n\n'
    rodape = f'\nSaldo - R$: {saldo:.2f}\n\n{"="*30}'
    print(cabecalho, extrato, rodape)
    

menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
=> """

numero_operacoes = 0
saldo = 0
limite = 1500
extrato = f''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    op = (input(menu)).upper()
    
    if(op == 'D'):
        
        valor=float(input("Valor do depósito => R$: "))
        
        if(valor > 0):
            saldo += valor
            adicionarExtrato(valor, 'D')
            print('Valor depositado.')
        else:
            print('Valor inválido para realizar o depósito.')
        continue
    
    elif(op == 'S'):
        
        valor=float(input("Valor do saque => R$: "))
        
        if(valor > 0):
            if(valor <= saldo):
                if(numero_saques < LIMITE_SAQUES):
                    if(valor <= limite):
                        numero_saques+=1
                        limite -= valor
                        saldo -= valor
                        adicionarExtrato(valor, 'S')
                    else:
                        print('O valor excede o limite diário de saques. Aguarde até amanhã.')
                else:
                    print('Limite de número saques diário já atingido. Aguarde até amanhã.')
            else:
                print('Saldo insuficiente para realizar o saque.')       
        else:
            print('Valor inválido para realizar o saque.')
            
        continue
    
    elif(op == 'E'):
        
        printarExtrato(saldo)
            
        continue
    
    elif(op == 'Q'):
        
        break
     
    else:
        print('Operação inválida, por favor selecione novamente.')


