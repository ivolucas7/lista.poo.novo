class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3, nota4, nota5):

         self.matricula = matricula
         self.nome = nome
         self.nota1 = nota1
         self.nota2 = nota2
         self.nota3 = nota3
         self.nota4 = nota4
         self.nota5 = nota5
         
    def calcular_media (self):
        soma = self.nota1 + self.nota2 + self.nota3 + self.nota4 + self.nota5
        self.media = soma / 5
        print(f"A média de {self.nome} é: {self.media}")
        
        return self.media
    
    
        
    def verificar_aprovaçao(self):
        media = self.calcular_media()
        if self.media >=7:
            print(f"{self.nome} aprovado")
            
        else:
            print(f"O {self.nome} foi reprovado")

aluno1 = Aluno(201030, "Sam", 6.0, 8.0, 9.5, 7.8, 9.1)
aluno2 = Aluno(201031, "Bem", 5.0, 7.0, 8.0, 7.0, 9.0)

aluno1.calcular_media()
aluno1.verificar_aprovaçao()
