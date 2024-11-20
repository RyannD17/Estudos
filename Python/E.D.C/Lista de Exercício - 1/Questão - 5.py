#Questão: Escreva um programa que leia dois números e mostre o maior.

número1 = int(input("Digite um número: "))
número2 = int(input("Digite outro número: "))
print()

if número1 > número2:
    print("O PRIMEIRO número digitado é MAIOR que o segundo!")

elif número1 < número2:
    print("O SEGUNDO número digitado é MAIOR que o primeiro!")

else:
    print("Os números digitados possuem o MESMO valor!")