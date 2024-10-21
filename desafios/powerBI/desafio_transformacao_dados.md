1- mudando cabeçalhos
	-> defini nomes baseados em sufixos como _depto, _func, _depend, _end, _prod e _proj
		(departamento, funcionário, dependente, endereço, produto e projeto)
	-> mngr = gerente, ssn= matricula, data_nasc

2- salario mudado p/ decimal fixo

3- decompus o endereço em numero, logradouro, cidade e estado

4- drill down em localizacao na tabela de departamento, mesclei os campos nome_depto e local_depto para torna-los unicos.

5- mesclei as tabelas employee e departament (juncao externa esquerda, através do campo numero_depto), criando uma nova "consulta" e renomeei para 'funcionario_departamento'

6- fiz drill down no departamento e selecionei apenas o nome e a matricula do manager

7- da tabela 'funcionario_departamento', deixei apenas os campos: matricula_func, nome_func, salario, matricula_mngr_func, numero_depto, nome_depto, matricuka_mngr_depto e as relações (talvez poderia deixar a localização do depto)

8- mesclei as tabelas employee e employee (juncao externa esquerda), criando uma nova "consulta" e renomeei para 'funcionario_gerente' (através dos campos matricula_mngr e matricula, respectivamente)

9- fiz drill down em employee atraves da matricula_mngr e deixei apenas os campos nome (mesclado com sobrenome) e matricula, tanto para funcionario, quanto para manager.

10- removi a linha inferior, que seria a do manager, pois como ele não possui gerente, nao faz sentido estar na relação