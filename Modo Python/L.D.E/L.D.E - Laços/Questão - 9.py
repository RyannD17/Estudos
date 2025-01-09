#Questão: Escreva um programa que leia um número inteiro n e mostre a tabuada de multiplicar de n.

n = int(input("Digite um número inteiro para ver sua tabuada de multiplicar: "))

print(f"\nTabuada de multiplicar de {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")