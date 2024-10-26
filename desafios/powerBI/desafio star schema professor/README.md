# Contexto
Resolução do desafio 'Dashboard de Vendas com Power BI utilizando Star Schema', do bootcamp oferecido pela NTTData, através da DIO, no módulo 'Modelagem de Dados com PowerBI'.

O enunciado encontra-se no arquivo '[Descrição do Desafio - Star Schema - Professor.docx](https://github.com/Otto-21/DIO/blob/main/desafios/powerBI/desafio%20star%20schema%20professor/Descri%C3%A7%C3%A3o%20do%20Desafio%20-%20Star%20Schema%20-%20Professor.docx)'

# Resolução
- Utilizei o site [SqlDBM](https://sqldbm.com/Home/) para realizar a modelagem, tanto do diagrama base, quanto do diagrama resolução em [Star Schema](https://learn.microsoft.com/pt-br/power-bi/guidance/star-schema).

- No diagrama base repliquei o que foi passado no enunciado e adicionei alguns campos de data para que eu conseguisse visualizar melhor a interação entre as tabelas e como elas seriam transformadas em [tabelas Dimensões](https://kb.ufla.br/books/termos-e-definicoes-governanca-de-dados/page/tabela-de-dimensao).

    ![image](https://github.com/user-attachments/assets/1a61a95f-d339-4fa7-a701-c4b1e98cde8d)


- Já no de resolução de desafio, como a tabela aluno ia ser desconsiderada, condensei as informações necessárias em cada uma das outras tabelas relacionadas direta e indiretamente a 'Professor'. Transferi as informações de pré requisito para a tabela 'D_Disciplina' e associei 'D_Curso' diretamente ao professor, para que não se tornasse um [Snowflake Schema](https://www.databricks.com/br/glossary/snowflake-schema). Assim, a tabela fato, 'F_Professor', é composta pelo seu id ([surrogate key](https://kb.ufla.br/books/termos-e-definicoes-governanca-de-dados/page/surrogate-key) da tabela), seu nome, e as chaves estrangeiras provindas de 'D_Disciplina', 'D_Curso', 'D_Data' e 'D_Departamento'.

    Vale salientar que a tabela 'D_Data' ficou responsável por conter a informação de quando o professor começou e terminou de ministrar tal disciplina, de certo curso, que pertence a certo departamento, além do semestre e do ano de oferta, para que haja maior granularidade dos dados a partir de data.

    ![image](https://github.com/user-attachments/assets/d0720f9f-a575-4c6e-900c-3947479b94e7)
