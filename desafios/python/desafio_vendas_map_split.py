def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas=0
    for contador, venda in enumerate(vendas): # enumerate começa no 0
      total_vendas+=venda
    
    media_vendas= total_vendas/(contador+1)
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    vendas= entrada.split(',')
    vendas= list(map(int, vendas))
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))