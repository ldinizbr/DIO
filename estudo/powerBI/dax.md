# O que é DAX?

- Data Analysis Expressions
- coleção de funções, operadores e constantes
	- podem ser usados em formulas ou expressões
	- retornam um ou mais valores
- influência no tamanho do .pbix
- não é bem compactada em relação a outros métodos

## O que essa linguagem permite?

* compilar medidas rápidas
* criar colunas calculadas
* compilar medidas
* interpretar como o contexto influencia as medidas
* manipular filtros (função CALCULATE)
* implementar inteligência de dados temporais

## O que são colunas calculadas?
* coluna não original
* agregação e funções matemáticas
* um valor para cada linha de chamada
(comentário) não afeta o tamanho do arquivo pbix, é calculada quando necessária

## O que são colunas personalizadas?
* transformação dos dados antes de importá-los
* cria-se na origem da consulta com SQL
* power query

## O que são medidas?
- úteis para operar linha à linha
- calculadas sob demanda, em cima dos filtros combinados, que dão contexto à informação

## No PowerBI 
- Medida Rápida (botão direito na aba campos)
 	* escolher cálculo a ser feito
 	* escolher atributo que servirá de valor base e o de categoria
  	* 'ok' - gera o dax / função x sem precisar escrever

- Nova medida (obotão direito na tabela específica)
	* nome_medida = função
 		- ex: Total Sales = SUM(finnancials[Sales])
   	* medidas e colunas não podem ser operadas juntas
  		- ex: dividir o Total Sales anterior por Units Solds (coluna da tabela)

## Coluna Personalizada
- dados cuja estrutura não é definida da mesma forma na fonte de origem
- pode ser criada:
	* na origem da obtenção (processamento no SGBD, puxado pelo BI)
	* com Power Query
   	* usando DAX (processamento no PowerBI)

## Contexto (!!!!!)
- possibilita a análise dinâmica
- afeta as medidas DAX
  	* mesma medida com resultados diferentes (por conta do contexto)
   	* ex: Total Sales pura, Total Sales por Ano, Total Sales por Produto
- tipos:
   	* #### de linha
   	  	- considera a linha atual
   	  	- segue relações entre as tabelas para determinar quais linhas estão relacionadas
   	* #### de consulta
   	  	- se refere ao subconjunto de dados recuperados implicitamente para uma formula
   	  	- ex: Vendas = SUM('Sales'[Profit])
   	* #### de filtro
   	  	- especifica restrições de filtros aos dados
   	  	- aplicado sobre outros contetos
   	  	- ex: ALLEXCEPT() 
