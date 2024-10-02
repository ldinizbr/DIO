def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
        if(contagem[produto]>max_count):
            max_count= contagem[produto]
            max_produto= produto
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    produtos= entrada.split(',')
    
    produtos= list(map(lambda x: x.strip(), produtos))

    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))
