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
