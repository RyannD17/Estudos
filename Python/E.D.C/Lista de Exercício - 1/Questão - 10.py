#Questão: Escreva um programa que leia dois números e informe se o maior é múltiplo do menor.

número1 = int(input("Digite um número: "))
número2 = int(input("Digite outro número: "))
print()

#Destacando qual número pode ser maior:
if número1 > número2:
    MAIOR = número1
    MENOR = número2

else:
    MAIOR = número2
    MENOR = número1

#Destacando se é ou não múltiplo:
if MENOR != 0:

    if MAIOR % MENOR == 0:
        print("O MAIOR número é múltiplo do MENOR!")
    else:
        print("O MAIOR número não é múltiplo do MENOR!")

else:
    print("Não há como verificar o número, pois o MENOR é zero!")