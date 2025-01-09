#Questão: Escreva um programa que leia um número inteiro positivo n, calcule e mostre a soma: 
# 1/1+1/2+1/3+1/4+...+1/(n-1)+1/n.

n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
    print("\nPor favor, insira um número inteiro positivo.")
else:
    soma = 0
    for i in range(1, n + 1):
        soma += 1 / i
    print(f"\nA soma da série é: {soma:.4f}")

# Explicação:
# Essa questão lida com uma sequência de acordo com o valor digitado pelo usuário.
# Se digitarmos 5, por exemplo, vêmos que ocorre:
    # 0 + 1/1 = 1;
    # 1 [número gerado] + 1/2 = 1.5
# Essa fração de [1/1, 1/2, 1/3, ...] se estende até o número digitado pelo usuário. Como podem ver, é descrito pelo denominador.