velocidade = float(input("Qual a velocidade atual do carro? "))
print()

if velocidade > 80:
    print("MULTADO! Você ultrapassou o limite permitido que é de 80km/h")
    multa = (velocidade - 80) * 7
    print("Você deve pagar uma multa de {}R$".format(multa))
    print()

print("Tenha um bom dia! Dirija com segurança!")