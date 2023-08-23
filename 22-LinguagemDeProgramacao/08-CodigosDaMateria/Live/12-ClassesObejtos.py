class Pessoa:
    def __init__(self, nome, idade): # Pode ser chamado de construtor
        self.nome = nome             # Não é obrigatorio usar mas é boa pratica
        self.idade = idade

    def saudacao(self): # Função printa a mensagem quando solicitada pelo objeto
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("Alice", 30)   # Criando objetos da classe Pessoa
pessoa2 = Pessoa("Bob", 25)

pessoa1.saudacao()              # Chamando o método saudacao para cada objeto
pessoa2.saudacao()

