#Dicionários: As estruturas de dados que possuem um mapeamento entre 
# uma chave e um valor são consideradas objetos do tipo mapping. 
# Em Python, o objeto que possui essa propriedade é o dict (dicionário). 
# Tal objeto é mutável, ou seja, com ele conseguimos atribuir 
# um novo valor a uma chave já existente.

# Em Python, uma das maneiras de criar um objeto do tipo dicionário é colocando as chaves e os valores entre estas, conforme código a seguir:
cadastro = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# Para acessar um valor em um dicionário, basta digitar:
# nome_dicionario[chave]
print(cadastro['nome'])

# E, para atribuir um novo valor, use:
# nome_dicionario[chave] = novo_valor
cadastro['nome'] = 'Rapha'
print(cadastro['nome'])