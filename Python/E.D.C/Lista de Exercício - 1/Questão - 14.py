#Questão: Escreva um programa que leia 4 números e mostre o maior.

número1 = int(input("Digite o PRIMEIRO número: "))
número2 = int(input("Digite o SEGUNDO número: "))
número3 = int(input("Digite o TERCEIRO número: "))
número4 = int(input("Digite o QUARTO número: "))
print()

if número1 > número2 and número1 > número3 and número1 > número4:
    print("O PRIMEIRO número digitado é MAIOR que os demais!")

elif número2 > número1:
    print("O SEGUNDO número digitado é MAIOR que o primeiro!")

else:
    print("Os números digitados possuem o MESMO valor!")