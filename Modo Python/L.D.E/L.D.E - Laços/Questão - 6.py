#Questão: Escreva um programa que leia dois números inteiros m e n e gere um vetor (array) contento n elementos, contendo a sequencia de m até m+n.

m = int(input("Digite o valor de m: "))
n = int(input("Digite o valor de n: "))

vetor = [m + i for i in range(n)]

print(f"\nVetor gerado: {vetor}")

# Explicação:
# Neste "vetor" temos "m + i". Este "i" será o índice que vai mudar de valor a cada iteração do laço, indo de 0 até o valor de "n" - 1.