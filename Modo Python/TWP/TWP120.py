#Questão: Pergunte a velocidade de um carro, supondo um valor inteiro. Caso ultrapasse 110 km/h, exiba uma mensagem dizendo que o usuário foi multado. Neste caso, exiba o valor da multa 5,00R$ por km acima de 110.

velocidade = int(input("Qual a velocidade percorrida pelo seu carro? "))
print()

if velocidade <= 110:
    print("Siga em frente!")
else:
    multa = (velocidade - 110) * 5
    print("Multado! Você ultrapassou o limite de velocidade e está penalizado com uma multa de {:.2f}R$".format(multa))