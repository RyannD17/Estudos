#Questão: Escreva um programa que leia um número inteiro e mostre o fatorial do mesmo.

n = int(input("Digite um número inteiro: "))

fatorial = 1 # Começando com 1, pois qualquer valor multiplicado por 1 é ele mesmo.

for i in range(1, n + 1): # O laço vai de 1 até n, multiplicando-os consecutivamente.
    fatorial *= i         # Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120.

print(f"O fatorial de {n} é {fatorial}")

# Explicação:
# O "range(1 (start), n + 1 (stop))" é o início da sequência até o número digitado (n).
# Adicionamos "n + 1" porque ele termina um valor antes, como se fosse um "n - 1" por isso, o uso do "+ 1".