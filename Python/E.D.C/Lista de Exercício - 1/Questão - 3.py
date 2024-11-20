#Questão: Escreva um programa que leia um número e mostre se ele é positivo.

número = int(input("Digite um número: "))

if número > 0:
    print("O número digitado é POSITIVO!")

elif número < 0:
    print("O número digitado é NEGATIVO!")

else:
    print("O número {} não é POSITIVO nem NEGATIVO!".format(número))