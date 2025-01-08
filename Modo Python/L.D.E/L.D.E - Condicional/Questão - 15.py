#Questão: Escreva um programa que leia dois nomes e informe se os mesmos são iguais. Além de informar se os nomes são iguais ele deve informar se há diferenças na digitação de letras maiúsculas/minúsculas. DICA: use o método upcase de String.

nome_1 = input("Digite o primeiro nome: ")
nome_2 = input("Digite o segundo nome: ")

if nome_1 == nome_2:
    print("Os nomes são exatamente iguais!".format(nome_1, nome_2))
else:
    # Declarando se há diferença entre maiúsculas/minúsculas
    if nome_1.upper() == nome_2.upper():
        print("Os nomes são iguais, mas há diferenças na digitação de maiúsculas/minúsculas.")
    else:
        print("Os nomes são diferentes.")