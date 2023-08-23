class Calculadora:
    def soma(self, x, y):
        v = x + y
        return v

    def subtrair(self, x, y):
        r = x - y
        return r

    def dividir(self, x, y):
        r = x / y
        return r

    def multiplicar(self, x, y):
        r = x * y
        return r


calculadora = Calculadora()

a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))

s = calculadora.soma(a, b)
print(f'A soma de {a} + {b} é igual a {s}')

s1 = calculadora.subtrair(a, b)
print(f'A subtração de {a} - {b} é igual a {s1}')

s2 = calculadora.dividir(a, b)
print(f'A divisão de {a} / {b} é igual a {s2}')

s3 = calculadora.multiplicar(a, b)
print(f'A multiplicação de {a} * {b} é igual a {s3}')

