#Questão: Escreva um programa que mostre todos os números entre 1 e 100 que são múltiplos de 3 e 7.

print("Números entre 1 e 100 que são múltiplos de 3 e 7.")
print("\nMúltiplos de 3:")

for i in range(1, 101):
    if i % 3 == 0:
        print(f"{i} -> ", end="")
print("FIM")

print("\nMúltiplos de 7:")

for i in range(1, 101):
    if i % 7 == 0:
        print(f"{i} -> ", end="")
print("FIM")

print("\nNúmeros entre 1 e 100 que são múltiplos de 3 e 7 ao mesmo tempo:")

for i in range(1, 101):
    if i % 3 == 0 and i % 7 == 0:
        print(f"{i} -> ", end="")
print("FIM")