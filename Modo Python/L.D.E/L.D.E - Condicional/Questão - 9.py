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

#Parece confuso, mas o que o código está fazendo é o seguinte:
# 1o - O valor digitado deve estar entre (0 e 360) e dizer o total de voltas dadas.

# 20 - Qualquer ângulo maior que 360 COMPLETOU UMA VOLTA, mas para sabemos quantas voltas foram dadas é só pegar o valor digitado pelo usuário e dividí-lo por 360 (ângulo // 360). Como o número é inteiro, neste exemplo: (720 // 360 = 2), o total "2" simboliza as VOLTAS COMPLETAS. Se fosse (450 // 360 = 1 [1,25]) o "1,25" é a resposta, porém, como a resposta deve ser inteira, o valor vira "1", consequentemente, dando um tatal de "1" volta.