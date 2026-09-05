"""Criando uma classe"""

class Carro:

    def __init__(self,cor,marca,linha,combustivel):
        self.cor = cor
        self.marca = marca
        self.linha = linha
        self.combustivel = combustivel

""" Criar um objeto"""
polo = Carro("branco", "volkswagen","Polo","gasolina")
mustang = Carro("verde","ford", "mustang", "gasolina")
prius = Carro("vermelho","toyota","prius", "eletrico")
golf = Carro("azul","volkswagen","golf","disel")


"""Mostrando informacoes na tela do objeto"""

print(f"A cor do {prius.linha} é {prius.cor}")


"""Mostrando na tela"""

print("O carro tem o nome de:",polo.linha)

print("O tipo de combustivel do carro Polo é:",polo.combustivel)

print("A cor do carro Polo é:",polo.cor)

print("A marca do carro Polo é:",polo.marca)






