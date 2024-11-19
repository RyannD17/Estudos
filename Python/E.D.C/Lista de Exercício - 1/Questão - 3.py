#Questão: Escreva um programa que leia um número e mostre se ele é positivo.

número = int(input("Digite um número: "))

if número % 2 == 0:
    print("O número digitado é POSITIVO!")
else:
    print("O número digitado é NEGATIVO!")