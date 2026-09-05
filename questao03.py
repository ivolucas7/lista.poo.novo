class Pessoa :
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


pessoa1 = Pessoa("Mosquito", "18","-10kg","1.60")
print(pessoa1)