# nome = input("Digite seu nome: ")
# peso = input("Digite seu peso: ").replace(',', '.')
# altura = input("Digite sua altura em Cm: ")
# alturaMetros = float(altura) / 100
# imc = float(peso) / (float(alturaMetros) * float(alturaMetros))
# if imc < 18.49:
#     print(f'{nome}, seu IMC e: {imc:.2f}, Seu IMC esta abaixo do peso')
# elif imc >= 18.5 or imc <= 24.5:
#     print(f'{nome}, seu IMC e: {imc:.2f}, Seu IMC esta normal')
# else:
#     print(f'{nome}, seu IMC e: {imc:.2f},Seu IMC esta acima do peso')
# print("Parabens por se preocupar com sua saude",nome)

lista = [1 ,2 ,3 ,4 ,5]      # Criei uma Lista com 5 numeros
tamanhoDaLista = len(lista)  # O len vai contar os itens da lista
print(tamanhoDaLista)        # Faz o Print do que o len contou