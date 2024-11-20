#Questão: Brincadeira do ímpar ou par: escreva um programa que leia dois nomes e dois valores inteiros, que correspondem ao que cada um colocou, e informe quem ganhou o “ímpar ou par”.

from time import sleep #O import "sleep" é usado para dar uma pausa no programa

print("-=-" * 30) #Apenas para destacar
pessoa_1 = input("Bem-vindo(a) a brincadeira do ímpar ou par! Digite o nome da primeira pessoa: ")
print()
pessoa_2 = input("Bem-vindo(a) a brincadeira do ímpar ou par! Digite o nome da segunda pessoa: ")

print("-=-" * 30) #Apenas para destacar

while True:
    escolha = input("Por favor {}, escolha entre ímpar ou par: ".format(pessoa_1))
    print()

    if escolha == "ímpar":
        print("{} escolheu ímpar! Logo, {} será par!".format(pessoa_1, pessoa_2))
        escolha_pessoa_1 = "ímpar"
        escolha_pessoa_2 = "par"
        break

    elif escolha == "par":
        print("{} escolheu par! Logo, {} será ímpar!".format(pessoa_1, pessoa_2))
        escolha_pessoa_1 = "par"
        escolha_pessoa_2 = "ímpar"
        break

    else:
        print("Inválido! Corrija sua escolha entre 'ímpar' ou 'par'!")

print("-=-" * 20) #Apenas para destacar
valor_1 = int(input("{}, escolha um valor. Aliás, seja rápido(a): ".format(pessoa_1)))
print()
valor_2 = int(input("{}, escolha um valor. Aliás, seja rápido(a): ".format(pessoa_2)))

print()
print("PROCESSANDO...")
sleep(3)

print("-=-" * 20) #Apenas para destacar
soma = valor_1 + valor_2
print("A soma dos valores é {}!".format(soma))
print()

if soma % 2 == 0:
    vencedor = pessoa_1 if escolha_pessoa_1 == "par" else pessoa_2
else:
    vencedor = pessoa_1 if escolha_pessoa_1 == "ímpar" else pessoa_2

print("Portanto, meus parabéns {}, você venceu!".format(vencedor))

#Vamos às explicações:

# 1o - Os dois usuários digitarão seus nomes. Depois, deixei que o primeiro usuário pudesse decidir entre "ímpar" ou "par". Porém, nesta condição, o segundo usuário escolhe por último o valor inteiro que decidirá o campeão. Logo após, processa o resultado da SOMA e exibe o VENCEDOR da brincadeira!

# 2o - SOBRE CONDICIONAIS:
# A primeira condicional, em outras palavras, nos diz que: SE o usuário (primeiro usuário, como mencionei) escolher "ímpar", RESULTARÁ "par" para o outro usuário.
# A segundo condicional, em outras palavras, nos diz que: SE a soma dos valores escolhidos forem "par", o usuário que a escolheu ganha o jogo; caso contrário, ele perde. ESSA É A BRINCADEIRA!

# 3o - Utilizei o "loop" (laço) para quando o usuário errar na digitação da escolha "ímpar" ou "par", ele retorna a opção de "ESCOLHA ÍMPAR OU PAR". Já o "break" é para que quando houver um erro e eu já consertá-lo, ele retoma à brincadeira. Em outras palavras, ele para o "loop" (laço de repetição), pois o erro já foi resolucionado.