import random
n1 = str(input("Primeiro nome: "))
n2 = str(input("Segundo nome: "))
n3 = str(input("Terceiro nome: "))
n4 = str(input("Quarto nome: "))

lista = [n1, n2, n3, n4]
random.shuffle(lista) # O "random.shuffle" é usado para que o computador embaralhar o que se pede.
print(f"\nA ordem de apresentação será: ")
print(lista)