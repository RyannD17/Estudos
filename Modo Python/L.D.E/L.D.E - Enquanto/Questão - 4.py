#Questão: Em Ruby, para a geração de um número aleatório usamos o método rand(MAX), onde MAX determina o valor máximo a ser gerado.
#Exemplo: par gerar um número entre 0 e 100 podemos aplicar a seguinte linha
#num = rand(100)
#Escreva um programa (jogo) que gere um número entre 0 e 1000 e peça para o usuário adivinhar o número. A cada tentativa o programa informa se o número informado pelo usuário é maior ou menor que o número a ser descoberto. Ao final o programa deve informar quantas tentativas foram feitas até a descoberta do número.

import random

numero_secreto = random.randint(0, 1000)
tentativas = 0

while True:
    tentativa = int(input("Adivinhe o número entre 0 e 1000: "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("O número é maior!")
        print()
    elif tentativa > numero_secreto:
        print("O número é menor!")
        print()
    else:
        print(f"\nPARABÉNS! Você acertou o número em {tentativas} tentativas.")
        break

# Explicação:
# O uso do "random.randint(0, 1000)" é para ser sortido um número aleatório.
# "random" é o módulo responsável por sortir os números nessa questão.
# "randint" é uma função do módulo "random" para que o número sortido seja um número INTEIRO.