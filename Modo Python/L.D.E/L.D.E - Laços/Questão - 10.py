#Questão: Escreva um programa que leia dois números inteiros a e b, de uma equação do primeiro grau na forma f(x)=ax+b. O programa deve mostrar todos os valores de f(x) e x para o intervalo de 0 a 100, separados por vírgula, um par por linha.

a = int(input("Digite o valor para o coeficiente a: "))
b = int(input("Digite o valor para o coeficiente b: "))

print("\nValores de f(x) para x no intervalo de 0 a 100:")

for x in range(101):
    fx = a * x + b
    print(f"x = {x}, f(x) = {fx}")