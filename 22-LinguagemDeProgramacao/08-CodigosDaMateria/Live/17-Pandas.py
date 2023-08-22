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

data = { # Criar um DataFrame
    'Nome': ['Alice', 'Raiana', 'Carol'],
    'Idade': [25, 30, 28],
    'Curso': ['Engenharia', 'ADS', 'Economia']
}

df = pd.DataFrame(data)
print("DataFrame:\n",(df))

idade_maior_que_25 = df[df['Idade'] > 25] # Filtrar o DataFrame por idade
print("\nPessoas com idade maior que 25:",(idade_maior_que_25)) # Exibir o DataFrame filtrado