#Questão: Escreva um programa que leia um números inteiro que corresponde a um ângulo e informe em qual quadrante este ângulo se encontra e quantas voltas ele dá (360 graus = uma volta).

ângulo = int(input("Digite um ângulo em graus: "))
print()
voltas = ângulo // 360

if 0 <= ângulo < 90:
    quadrante = "PRIMEIRO QUADRANTE"

elif 90 <= ângulo < 180:
    quadrante = "SEGUNDO QUADRANTE"

elif 180 <= ângulo < 270:
    quadrante = "TERCEIRO QUADRANTE"

elif 270 <= ângulo < 360:
    quadrante = "QUARTO QUADRANTE"

else:
    quadrante = "EIXO POSITIVO do X"

print("O ângulo {} está no {}!".format(ângulo, quadrante))
print("O ângulo corresponde a um total de {} voltas!".format(voltas))