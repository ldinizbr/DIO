# Contexto
Desafio proposto pela DIO no bootcamp oferecido pela NTT Data, no módulo de curso "Modelando um Dashboard de E-commerce com Power BI Utilizando Fórmulas DAX".

O enunciado se encontra no arquivo '[desafio proposto.docx](https://github.com/Otto-21/DIO/blob/main/desafios/powerBI/desafio%20star%20schema/desafio%20proposto.docx)' e a sample base foi a 'finnancials', oferecida pelo próprio PowerBI.

# Etapas
## Transformação de Dados
1. Para o começo do processo de modelagem, ajustei os tipos de dados da tabela 'finnancials', de decimais para decimais fixos, quando necessário.
   
2. Criei duplicatas da tabela e renomeei a original para 'finnacials_origem'.
  
3. Na primeira duplicata, nomeei-a 'D_Produtos', fiz o agrupamento avançado dos registros pelo campo 'Product' e fiz agregações:
    - 'contagem': contou o total de linhas de registros por produto
    - 'valor maximo vendas': calculou o valor maximo de 'Sales' por produto
    - 'valor minimo vendas': calculou o valor minimo de 'Sales' por produto
    - 'media de valor de vendas': calculou a media de 'Sales' agrupada por produto
    - 'mediana do valor de vendas': calculou a mediana de 'Sales' agrupada por produto
    - 'media de manufatura': calculou a media de 'Manufacturing Price' agrupada por produto
      
    Após isso, inseri uma coluna de índice a partir de 0, renomeei para 'id_produto' e ordenei as colunas como achei necessário.

4. Na segunda, nomeei-a 'D_Descontos', removi todas as colunas, exceto 'Product', 'Discount Band' e 'Discounts', adicionei uma coluna condicional, substituindo os valores de 'product' pelos seus respectivos ids, criados na tabela 'D_Produtos' e então removi a coluna 'product'.
    Ordenei as linhas de forma crescente por 'id_produto', 'Discount Band' e 'Discounts' e então inseri uma coluna de índice, chamada 'id_descontos'.

5. Na terceira, 'D_Produtos_Detalhes', deixei somente as colunas 'Product', 'Units Solds', 'Manufacturing Price', 'Sale Price' e 'Discount Band'. Usei-as na mesma sequência para ordenar os registros de forma crescente, com exeção da coluna 'Manufacturing Price'. Inseri uma coluna índice, 'id_produto_detalhes', substitui a coluna 'Product' pelos seus ids e removi a anterior. Também inclui uma coluna personalizada que calcua o valor total da venda:
   
```
Total Sale Price = Table.AddColumn(#"Tipo Alterado", "Personalizar", each [Sale Price]*[Units Sold])
```
6. Na quarta, 'D_Detalhes' (detalhes de vendas), deixei as colunas 'Segment', 'Country', 'Product', 'Gross Sales', 'Sales', 'COGS' e 'Profit', ordenei de forma crescente por 'Product', 'Segment', 'Country' e 'Sales' e inseri uma coluna índice do 0, nomeado 'id_detalhes'.

7. Na tabela fato, 'F_Vendas', removi 'COGS', 'Month Number', 'Manufacturing Price' e 'Gross Sales' e adicionei um índice, 'SK_id' (Surrogate Key).
    Para conseguir adicionar os devidos ids para as chaves estrangeiras 'id_detalhes', 'id_descontos' e 'id_produto_detalhes', fiz a ordenação da tabela de acordo com a ordenação de cada uma das respectivas tabelas, fui inserindo indices e renomeando-os de acordo, pois o PowerBI não permite o relacionamento por mais de um campo.
    Por fim, substitui 'Product' por 'id_produto'.

8. Conferi novamente os tipos de dados, ajustei quando necessário e mudei a disposição das colunas para visualização.

9. Fechei e apliquei as alterações.

10. Já em 'Exibição de Modelo', inseri uma nova tabela 'D_Data', com o código em DAX:
```
D_Data = 
    ADDCOLUMNS(
        CALENDAR(DATE(2013, 1, 1), DATE(2014, 12, 31)),
        "Year", YEAR([Date]),
        "Month", MONTH([Date]),
        "Month Name", FORMAT([Date], "MMMM"), "Data", FORMAT([Date], "dd/mm/yyyy")
    )
```
> deixei as datas entre 2013 e 2014, pois os dados da tabela base estão nesse intervalo.

  Para o [Star Schema](https://learn.microsoft.com/pt-br/power-bi/guidance/star-schema), uma tabela de datas é essencial para a análise temporal dos dados, graças a consistência e granularidade de dados que ela confere.

## Relacionamentos
1. Em 'Exibição de Modelo', removi todos os relacionamentos que haviam sido criados automaticamente e os adequei da seguinte forma:
   
   ![image](https://github.com/user-attachments/assets/f0373e11-c98c-4278-9558-a63796bab6c9)

2. Ocultei 'finnancials_origem'

3. Resultando no modelo:

   ![image](https://github.com/user-attachments/assets/bd798830-2b01-41f8-8ede-5d725346f814)
