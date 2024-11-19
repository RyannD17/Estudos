#Questão: Escreva um programa que leia 4 números e mostre o maior.

número1 = int(input("Digite o PRIMEIRO número: "))
número2 = int(input("Digite o SEGUNDO número: "))
número3 = int(input("Digite o TERCEIRO número: "))
número4 = int(input("Digite o QUARTO número: "))
print()

maior = número1

if número2 > maior:
    maior = número2

elif número3 > maior:
    maior = número3

elif número4 > maior:
    maior = número4

print("O MAIOR número digitado é {}!".format(maior))