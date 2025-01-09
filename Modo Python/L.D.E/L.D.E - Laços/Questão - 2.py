#Questão: Escreva um programa que leia um número inteiro n e um nome. O programa deve mostrar o nome n vezes, cada um em uma linha.

n = int(input("Digite um número inteiro: "))
nome = input("Digite um nome: ")

for i in range(n): # O "+1" é para incluir o número digitado.
    print(f"{nome} -> ", end="")
print("FIM")