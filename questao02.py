class Livro :
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano 


livro1 = Livro("Dom Casmurro", "Machado de Assis" ,"1899") 

print(f"O titulo do livro é {livro1.titulo}, e o autor é o {livro1.autor} e teve seu lançamento no ano de {livro1.ano}")      