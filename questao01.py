class Bola :
    def __init__ (self,cor,circuferencia,material,esporte):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material 
        self.esporte = esporte

bola1 = Bola("verde","30cm","plastico","futebol")
bola2 = Bola("azul","50cm", "borracha","volei")

print(f"A bola1 é de {bola1.esporte} ")
       
                