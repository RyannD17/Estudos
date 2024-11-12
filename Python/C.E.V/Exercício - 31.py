distância = float(input("Qual a distância da sua viagem? "))
print()
print("Você está prestes a começar uma viagem de {}km.".format(distância))
print()

if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45

print("E o preço da sua viagem é de {:.2f}R$".format(preço))