#Questão: Escreva um programa que leia dois números n e m. O programa deve mostrar todos os números menores que m que sejam múltiplos de n.

n = int(input("Digite o primeiro número: "))
m = int(input("Digite o segundo número: "))

print(f"\nNúmeros menores que {m} que são múltiplos de {n}:")

for i in range(m):
    if i % n == 0:
        print(f"{i} -> ", end="")
print("FIM")