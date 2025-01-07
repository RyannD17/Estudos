#Questão: Escreva um programa que leia um número inteiro que corresponde a um ângulo e informe em qual quadrante este ângulo se encontra.

ângulo = int(input("Digite um ângulo em graus: "))
print()
ângulo = ângulo % 360

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

#Parece confuso, mas o que o código está fazendo é o seguinte:
# 1o - O valor digitado deve estar entre (0 e 360)

# 20 - Qualquer ângulo que divido por 360 o resto seja 0 (0 pertence ao primeiro quadrante e ao eixo de x), ele será múltuplo de 360; caso contrário, se o resto for 1 (1 pertence ao primeiro quadrante, mas não ao eixo de x) ele não será 0 nem múltiplo de 360, mas estará no primeiro quadrante.

# 3o - Se o número não estiver entre esses valores (o uso do else), ele terá somente três opções: É zero; Múltiplo de 360; Pertencerá ao primeiro quadrante.