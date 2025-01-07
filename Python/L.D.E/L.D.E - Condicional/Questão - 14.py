#Questão: Escreva um programa que leia 4 números e mostre o maior.

número1 = int(input("Digite o PRIMEIRO número: "))
número2 = int(input("Digite o SEGUNDO número: "))
número3 = int(input("Digite o TERCEIRO número: "))
número4 = int(input("Digite o QUARTO número: "))
print()

maior = número1 #Destacando o MAIOR número

if número2 > maior: #Destacando as possíveis mudanças do MAIOR número, ou seja, o 1o número é MENOR comparado ao 2o nesta mudança, e com o 3o e 4o número também foi destacado dessa forma afim de realizar a questão
    maior = número2

elif número3 > maior:
    maior = número3

elif número4 > maior:
    maior = número4

print("O MAIOR número digitado é {}!".format(maior))