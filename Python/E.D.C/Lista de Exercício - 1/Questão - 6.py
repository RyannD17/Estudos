#Questão: Escreva um programa que leia dois nomes e mostre o que contém maior quantidade de caracteres.

nome1 = input("Digite um nome: ")
nome2 = input("Digite outro nome: ")
print()

if len(nome1) > len (nome2): #O "len" em py 
    print("O PRIMEIRO nome digitado possue mais caracteres que o segundo!")

elif len(nome2) > len(nome1):
    print("O SEGUNDO nome digitado possue mais caracteres que o primeiro!")

else:
    print("Os nomes digitados possuem o MESMO valor de caracteres!")