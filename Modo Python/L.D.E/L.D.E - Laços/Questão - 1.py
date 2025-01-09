#Questão: Escreva um programa que leia um número inteiro n e mostre todos os números entre 0 e n.

n = int(input("Digite um número inteiro: "))

for i in range(n + 1): # O "+1" é para incluir o número digitado.
    print(f"{i} -> ", end="")
print("FIM")

# Explicação:
# O "range()" cria uma sequência de números, começando de 0 até "n".
# O "for" percorre a sequência de números de 0 até n e imprime cada número (i).
# Este "i" é a variável que vai receber cada número da sequência.