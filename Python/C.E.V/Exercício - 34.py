salário = float(input("Qual é o salário do funcionário? "))
print()

if salário <= 1250:
    novo = salário + (salário * 15/100) #Aqui estou fazendo um estilo de "PORCENTAGEM", no qual eu multiplico o salário dado pelo usuário com a porcentagem que a questão me fornecer. Neste caso, o valor foi de 15%, e na prática para o cálculo eu deixo dessa forma: (salário * 15/100), onde MEU SALÁRIO SOMA COM O (SALÁRIO MULTIPLICADO PELA FRAÇÃO DE 15 POR 100 (15%))
else:
    novo = salário + (salário * 10/100) #O mesmo vale para esse caso, pois o valor foi de 10%, e na prática para o cálculo eu deixo dessa forma: (salário * 10/100), onde MEU SALÁRIO SOMA COM O (SALÁRIO MULTIPLICADO PELA FRAÇÃO DE 10 POR 100 (10%))

print("Quem ganhava {:.2f}R$ passa a ganhar {:.2f}R$ agora.".format(salário, novo))