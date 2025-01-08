casa = float(input("Qual o valor da casa? "))
salário = float(input("Qual o salário do comprador? "))
anos = int(input("Quantos anos de financiamento? "))

prestação = casa / (anos * 12)
mínimo = salário * 30/100

print("Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}.".format(casa, anos, prestação))

if prestação <= mínimo:
    print("Empréstimo CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")