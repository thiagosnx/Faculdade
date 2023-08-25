''' A biblioteca pandas é uma das bibliotecas mais populares em Python para análise e manipulação de dados. 
Ela oferece estruturas de dados e funções eficientes para trabalhar com dados em tabelas, séries temporais 
e outras estruturas semelhantes a planilhas. O pandas é amplamente utilizado em tarefas como limpeza de dados, 
análise exploratória, processamento de dados, transformação e visualização.
As duas principais estruturas de dados fornecidas pelo pandas são: '''

# DataFrame: É uma estrutura bidimensional semelhante a uma tabela, onde cada coluna pode conter 
# diferentes tipos de dados. Um DataFrame é especialmente útil para representar dados tabulares 
# e é comparável a uma planilha do Excel ou a uma tabela de um banco de dados.

# Series: É uma estrutura unidimensional que representa uma única coluna de dados. 
# Uma Series pode ser vista como uma lista indexada.

import pandas as pd

# Exemplo de DataFrame
data = {'Nome': ['Rapha', 'Naty', 'Tiago'],
        'Idade': [25, 30, 22]}

df = pd.DataFrame(data)
print("DataFrame:\n",(df))

# Acessando uma coluna inteira
coluna_nome = df['Nome']
print(coluna_nome)

# Acessando um valor específico
valor_idade = df.at[1, 'Idade']
print(valor_idade)

# Acessando uma linha inteira
linha_0 = df.iloc[0]
print(linha_0)

# Acessando um valor específico usando índices numéricos
valor_nome_2 = df.iloc[2, 0]
print(valor_nome_2)

# Acessando um valor específico por rótulos de índice
valor_nome_Rapha = df.loc[0, 'Nome']
print(valor_nome_Rapha)

# Substituindo o nome "Alice" por "Eva"
novo_nome = 'Ezequiel'
df.loc[df['Nome'] == 'Rapha', 'Nome'] = novo_nome

print("DataFrame:\n",(df))

#-----------------------------------------------------
# Tipos de dados que podem ser extraidos de uma series

series_dados = pd.Series([10.2, -1, None, 15, 23.4])
print("Quantidade de linhas = ", series_dados.shape) # Retorna uma tupla com o numero de linhas
print("Tipo de dados = ", series_dados.dtype)# Retorna o tipo de dados, se for misto será object
print("Os valores sao unicos? ", series_dados.is_unique)# Verifica se nao tem duplicidade
print("Existem valores nulos?", series_dados.hasnans)# Verifica se há valores nulos
print("Quantos valores existem?", series_dados.count())# Conta a quantidade de valores
#-----------------------------------------------------
# Tratando funções matematicas e estatisticas
print("Qual o menor valor? ", series_dados.min())# Extrai o menor valos
print("Qual o maior valor? ", series_dados.max())# Extrai o maior valor
print("Qual a média dos valores? ", series_dados.mean())# Extrai a média
print("Qual o desvio padrao? ", series_dados.std())# Extrai o desvio padrao
print("Qual a mediana? ", series_dados.median())# Extrai a mediana
print("\nResumo\n", series_dados.describe())# Exibe o resumo sobre os dados
