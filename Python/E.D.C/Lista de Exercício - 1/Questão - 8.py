#Questão: Escreva um programa que leia um número inteiro que corresponde a um ângulo e informe em qual quadrante este ângulo se encontra.

ângulo = int(input("Digite um ângulo em graus: "))

if 0 <= ângulo < 90:
    print("O ângulo corresponde ao PRIMEIRO QUADRANTE!")

elif 90 <= ângulo < 180:
    print("O ângulo corresponde ao SEGUNDO QUADRANTE!")

elif 180 <= ângulo < 270:
    print("O ângulo corresponde ao TERCEIRO QUADRANTE!")

elif 270 <= ângulo < 360:
    print("O ângulo corresponde ao QUARTO QUADRANTE!")

else:
    print("O ângulo é 0 ou múltiplo de 360 e está no eixo positivo do X!")