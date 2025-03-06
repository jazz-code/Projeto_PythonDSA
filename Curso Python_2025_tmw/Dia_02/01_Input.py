#%%
print("Olá mundo")

nome = input("Digite seu nome: ")

print("Prazer, ", nome, ". Que legal te conhecer!")
#%%
#Dobro

numero = input("Digite um número: ")
numero = int(numero)
dobro = numero * 2
print("O dobro de ", numero, " é ", dobro)

#%%
#Exercicio
print("Bom dia !")
nome = input("Bom dia, qual é o seu nome: ")
print("Que legal te conhecer, ", nome, "!")

#%%
# input() sem variável aguarda ação do usuário e não armazena o valor
# ao colocar o input() e dentro a variável ele aguarda  ação do usuário e armazena o valor

numero = input("Digite um número inteiro: ")
numero = int(numero)
Raiz = numero ** (1/2) # ** 0.5
print("A raiz quadrada de ", numero, " é ", Raiz)

