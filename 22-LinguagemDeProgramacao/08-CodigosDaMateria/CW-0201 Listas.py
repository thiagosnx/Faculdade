# o primeiro valor ocupa a posição zero da lista, já o último ocupa a posição n – 1, 
# em que n é a quantidade de elementos que a lista é capaz de armazenar.

# Uma das maneiras de criar uma lista é colocando os valores entre colchetes.
vogais1 = ['a', 'e', 'i', 'o', 'u']

# A lista pode ser criada sem nenhum elemento, e a inserção pode ser feita posteriormente:
vogais2 = []
vogais2.append('a')
vogais2.append('e')
vogais2.append('i')
vogais2.append('o')
vogais2.append('u')

#Para acessar o valor guardado em uma lista, basta indicar o nome da variável e, 
# entre colchetes, a posição do elemento, ou a fatia (slice) de valores que se deseja:

vogais2[3]
vogais2[3:]