class Pessoa:
    def __init__(self, nome, idade): # Pode ser chamado com construtor
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("Alice", 30)   # Criando objetos da classe Pessoa
pessoa2 = Pessoa("Bob", 25)

pessoa1.saudacao()              # Chamando o método saudacao para cada objeto
pessoa2.saudacao()
