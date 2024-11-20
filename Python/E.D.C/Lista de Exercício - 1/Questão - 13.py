#Questão: Escreva um programa que leia um número real e faça o arredondamento para inteiro. Se a parte fracionária for maior do que 0.5 o arredondamento deve ser feito para o o próximo inteiro.

número = float(input("Digite um número real: "))
print()

inteiro = int(número)
fracionário = número - inteiro

if fracionário > 0.5:
    resultado = inteiro + 1
else:
    resultado = inteiro

print("O número {} arredondado para inteiro é igual a {}".format(número, resultado))