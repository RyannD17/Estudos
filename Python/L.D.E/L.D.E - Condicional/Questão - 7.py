#Questão: Escreva um programa que leia um número e informe se ele é positivo ou negativo.

número = int(input("Digite um número: "))
print()

if número > 0:
    print("O número digitado é POSITIVO!")

elif número < 0:
    print("O número digitado é NEGATIVO!")

else:
    print("O número digitado é ZERO!")