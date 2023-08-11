def busca_binaria(lista, elemento):
  minimo = 0
  maximo = len(lista) - 1
  encontrado = False
  indices = []

  while minimo <= maximo and not encontrado:
    meio_lista = (minimo + maximo) // 2
    indices.append(meio_lista)
    if lista[meio_lista] == elemento:
      encontrado = True
    else:
      if elemento < lista[meio_lista]:
        maximo = meio_lista - 1
      else:
        minimo = meio_lista + 1

  return encontrado, indices


def imprime_indices(indices):
  for i in indices:
    print(i)


testelista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
encontrado, indices = busca_binaria(testelista, 1)
if encontrado:
  print("Elemento encontrado!")
else:
  print("Elemento não encontrado.")
imprime_indices(indices)