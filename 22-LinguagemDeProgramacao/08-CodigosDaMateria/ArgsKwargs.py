def exemplo(*args, **kwargs):
    print("Argumentos posicionais:")
    for arg in args:
        print(arg)

    print("\nArgumentos de palavra-chave:")
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

exemplo(1, 2, 3, nome='Rapha', idade=36)
