"""Criando a class Pessoa"""
class Pessoa:
     def __init__(self,n,i,p,a): #dentro dos parenteses ficam os parametros que sao os valores que o usuario vai me fornecer
         self.nome = n #self .nome é o atributo que vai armazenar o parametro que o usuario forneceu
         self.idade = i
         self.peso = p
         self.altura = a
         
         
     def apresentaçao(self):
         print(f"O nome da pessoa consultada é {self.nome}; \nA idade dele(a) é: {self.idade};")
         
         
     def fazer_anivesario(self):
         self.idade +=1 #Esse metodo pega a idade do objeto e soma +1
         print(f"Feliz aniversario, {self.nome}!!!! Sua nova idade agora é:{self.idade}.")
         
"""Criando os OBJETOS  da classe pessoa""" 
pessoa1 = Pessoa("Grace", 30, 55, 1.60)
pessoa2 = Pessoa("Alan", 25, 70, 1.80)
         

"""Chamando os metodos """
pessoa1.apresentaçao()
pessoa1.fazer_anivesario()       
pessoa1.apresentaçao()
         
        
        
        
        
