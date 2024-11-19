#Questão: Escreva um programa que leia um número e mostre se ele é múltiplo de 7.

número = int(input("Digite um número: "))

if número % 7 == 0:
    print("O número digitado é multiplo de 7!")
else:
    print("O número digitado não é multiplo de 7!")