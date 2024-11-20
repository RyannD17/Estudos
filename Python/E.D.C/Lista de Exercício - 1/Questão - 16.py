#Questão: Escreva um programa que leia 3 números inteiros e mostre-os em ordem crescente.

número1 = int(input("Digite o PRIMEIRO número: "))
número2 = int(input("Digite o SEGUNDO número: "))
número3 = int(input("Digite o TERCEIRO número: "))
print()

if número1 <= número2 <= número3:
    ordem = (número1, número2, número3)

elif número1 <= número3 <= número2:
    ordem = (número1, número3, número2)

elif número2 <= número1 <= número3:
    ordem = (número2, número1, número3)

elif número2 <= número3 <= número1:
    ordem = (número2, número3, número1)

elif número3 <= número1 <= número2:
    ordem = (número3, número1, número2)

else:
    ordem = (número3, número2, número1)

print("A ordem crescente dos números digitados: {}".format(ordem))