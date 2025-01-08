#Questão: Escreva um programa que leia um número e mostre se ele é múltiplo de 7.

número = int(input("Digite um número: "))

if número % 7 == 0: #O símbolo da porcentagem no py retorna o resto da divisão de um número inteiro, e neste contexto, estou ordenando que para o número digitado pelo usuário ser múltiplo de 7, o resto da divisão dele tem que ser 0, caso contrário, o resto será 1, e consequentemente, não será múltiplo de 7.
    print("O número digitado é multiplo de 7!")
else:
    print("O número digitado não é multiplo de 7!")