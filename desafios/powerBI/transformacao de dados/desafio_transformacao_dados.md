# Transformação de Dados

1. mudando cabeçalhos
	- defini nomes baseados em sufixos como _depto, _func, _depend, _end, _prod e _proj
		(departamento, funcionário, dependente, endereço, produto e projeto)
	- mngr = gerente, ssn= matricula, data_nasc

2. salario mudado p/ decimal fixo

3. decompus o endereço do employee em numero, logradouro, cidade e estado

4. drill down em localizacao na tabela de departamento, mesclei os campos nome_depto e local_depto para torna-los unicos.

5. mesclei as tabelas employee e departament (juncao externa esquerda, através do campo numero_depto), criando uma nova "consulta" e renomeei para 'funcionario_departamento'

6. fiz drill down no departamento e selecionei apenas o nome e a matricula do manager

7. da tabela 'funcionario_departamento', deixei apenas os campos: matricula_func, nome_func, salario, matricula_mngr_func, numero_depto, nome_depto, matricuka_mngr_depto e as relações (talvez poderia deixar a localização do depto)

8. mesclei as tabelas employee e employee (juncao externa esquerda), criando uma nova "consulta" e renomeei para 'funcionario_gerente' (através dos campos matricula_mngr e matricula, respectivamente)

9. fiz drill down em employee atraves da matricula_mngr e deixei apenas os campos nome (mesclado com sobrenome) e matricula, tanto para funcionario, quanto para manager.

10. removi a linha inferior, que seria a do manager, pois como ele não possui gerente, nao faz sentido estar na relação.

11. eliminei colunas desnecessárias para o relatório.

12. para saber quantos fucnionários são atribuídos a cada gerente:
```
select e.Super_ssn as Ssn_mngr, CONCAT(e2.Fname,' ',e2.Lname) as name_mngr,
count(*) as total_employees
from employee e
left join employee e2 on e.Super_ssn = e2.Ssn
where e.Super_ssn is not null
group by e.Super_ssn;
```
