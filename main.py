#classe Animal ( Mãe )
class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print(self.som)
    def mudar_cor(self, nova_cor):
        self.cor = nova_cor
#Classe Elefante ( Filha )
class Elefante(Animal):
    def __init__(self, tamanho):
        self.tamanho = tamanho
    def trombar(self):
        print(self.som)
    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

#Entrada de dados
nome = input("Nome do Elefante: ")
idade = int(input("Idade do Elefante: "))
especie = input("Especie do Elefante: ")
cor = input("Cor do elefante: ")
tamanho = input("Tamanho do elefante: ")

som = ""

#Instanciando a classe Animal
animal = Animal(nome, idade, especie, cor, som)
#Instanciando a classe Elefante ( filha )
elefante = Elefante(tamanho)

if especie == "Africano" and idade < 10:
    elefante.tamanho = "pequeno"
    elefante.som = "Paah"
elif especie == "Africano" and idade >= 10:
    elefante.tamanho = "grande"
    elefante.som = "PAHHHHHH"


#Printando o tamanho do elefante
print("Tamanho: " + elefante.tamanho)


#Emitindo som através do método ca classe mãe
elefante.emitir_som()
#Emitindo som através da classe filha
elefante.trombar()

