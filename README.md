# Projeto-Avsys
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

##  &nbsp; Estruturas
  - Arvore AVL
  - Fila Encadeada com Nó Cabeça

## &nbsp; Objetos
  - Avião
  - Aeroporto
  - Vendas
  - Ticket

## &nbsp; Respostas Socket (Sucesso):
  - 001 -> Servidor Aberto
  - 002 -> Cliente Desconectado
  - 003 -> Comando Obter
  - 004 -> Comando Verificar
  - 005 -> Comando Comprar
  - 006 -> Cadeira comprada com sucesso! Verifique a sua compra com o comando VERIFICAR ID
  - 007 -> Saindo do Servidor...
 
 ## &nbsp; Respostas Socket (Erros):
  - Código 101 -> Erro!!! Digite o comando corretamente! 
  - Código 102 -> Digite dados válidos!
  - Código 103 -> ERRO! Avião inexistente ou inválido!
  - Código 104 -> Erro! Argumento Inválido!
  - Código 105 -> Digite dados válidos para realizar a verificação!
  - Código 106 -> Faltou o ID para realizar a verificação!
  - Código 107 -> Complete os parâmetros do comando corretamente!
  - Código 109 -> Assento já foi comprado!
  - Código 110 -> ERROR! Este ID de compra não existe!
  - Código 111 -> ERROR! Este ID do Avião não existe!

 ## &nbsp; Comandos:
  - Obter [arg1] = retorna os voos ou os ID de compras realizadas (arg1 = voos ou arg1 = id)
  - Verificar [arg1] [arg2] = retorna os dados de um voo, de uma compra ou os assentos disponíveis de um voo (arg1 = voo, arg1 = id ou arg1 = assentos) (arg2 = ID, arg2 = codigo do voo)
  - Comprar [arg1] [arg2] [arg3] = realiza a compra, porém verifica se o assento atual já não está ocupado (arg1 = nome do comprador) (arg2 = numero do assento) (arg3 = codigo do voo)
  
