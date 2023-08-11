# O interpretador Python possui o módulo built-in sqlite3, que permite utilizar 
# o mecanismo de banco de dados SQLite. Com esse módulo, é bastante simples 
# criar um banco de dados SQLite e fazer a conexão. 

# A seguir, criamos um banco de dados chamado aulaDB. 
# Esse comando criará um arquivo chamado aulaDB com extensão db, que o identifica como um arquivo de banco.

import sqlite3
conn = sqlite3.connect('aulaDB.db')

'''O CRUD no banco de dados SQLite'''
# Quando o assunto é banco de dados, um termo muito comum é o CRUD, 
# um acrônimo para as quatro operações de DML que podemos fazer em uma tabela no banco de dados
# podemos inserir informações (create), ler (read), atualizar (update) e apagar (delete). 

#Os passos necessários para efetuar uma das operações do CRUD são sempre os mesmos:
'''
1 - Estabelecer a conexão com um banco
2 - Criar um cursor e executar o comando
3 - Gravar a operação
4 - Fechar o cursor e a conexão'''

'''CREATE'''
#A variável conn guarda a instância de conexão com o banco de dados. Agora é preciso criar um cursor 
# para executar as instruções e, por fim, gravar as alterações com o método commit().
cursor = conn.cursor()
cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa A', '11.111.111/1111-11', 'São Paulo', 'SP', '11111-111', '2020-01-01')
""")
conn.commit()

'''READ'''
#Para ler os dados em uma tabela, também precisamos estabelecer uma conexão e criar um objeto
# cursor para executar a instrução de seleção. Ao executar a seleção, podemos usar o método 
# fetchall(), para capturar todas as linhas mediante uma lista de tuplas.
cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()
for linha in resultado:
    print(linha)
    
'''UPDATE'''
# Ao inserir um registro no banco, pode ser necessário alterar o valor de uma coluna,
# o que pode ser feito por meio da instrução SQL UPDATE.
cursor.execute("UPDATE fornecedor SET cidade = 'Campinas' WHERE id_fornecedor = 5")
conn.commit()  

'''DELETE'''
# Ao inserir um registro no banco, pode ser necessário removê-lo no futuro,
# o que pode ser feito por meio da instrução SQL DELETE.
cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = 2") 
conn.commit() 