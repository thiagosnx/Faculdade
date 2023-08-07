# algoritmo usado para buscar um valor em uma sequência é o de busca binária. 
# A primeira grande diferença entre o algoritmo de busca linear e o algoritmo
# de busca binária é que neste os valores precisam estar ordenados

'''A lógica é a seguinte:

1 - Encontra o item no meio da sequência.
2 - Se o valor procurado for igual ao item do meio, a busca encerra.
3 - Se não, verifica se o valor buscado é maior ou menor que o valor central.
4 - Se for maior, então a busca acontecerá na metade superior da sequência (a inferior é descartada), se não for maior, a busca acontecerá na metade inferior da sequência (a superior é descartada).
5 - Repete os passos: 1, 2, 3, 4.'''

def busca_binaria(lista, elemento):
        minimo = 0 
        maximo = len(lista)-1
        encontrado = False
    
        while minimo <= maximo and not encontrado:
            meio_lista = (minimo + maximo)//2
            if lista[meio_lista] == elemento:
                encontrado = True
            else:
                if elemento < lista[meio_lista]:
                    maximo = meio_lista-1
                else:
                    minimo = meio_lista+1
    
        return encontrado
    
testelista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(busca_binaria(testelista, 14))

# Linha 6 - Na linha 6, temos a estrutura de repetição “while”, 
# que será executada enquanto o primeiro elemento da lista (mínimo) 
# for menor ou igual ao máximo (último elemento) e o elemento procurado não for encontrado.

# Linha 7 - Na linha 7, identificamos o índice associado à metade da lista.

# Linha 8 - Na linha 8, temos uma estrutura de condição “if” em razão da qual, 
# basicamente, verifica-se que, se o elemento do meio da lista for o valor procurado, 
# será retornado o True (linha 9).

# Linha 10 - Na linha 10, temos a condição “else”, que verifica se o elemento procurado
# é menor que o valor do meio da lista. Se for maior, então a busca acontecerá na metade
# superior da sequência (a inferior é descartada); se não for, a busca acontecerá na
# metade inferior da sequência (a superior é descartada).

# Algoritmos de busca compõem o arsenal de algoritmos tradicionais da computação. 
# Quando é conhecida a sequência de passos, ou seja, o pseudocódigo, basta escolher
# uma linguagem de programação e implementá-la.