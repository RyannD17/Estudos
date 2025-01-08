#Questão: Considere a empresa de telefonia Tchau. Abaixo de 200 minutos, a empresa cobra 0,20R$ por minuto. Entre 200 e 400 minutos, o preço é 0,18R$. Acima de 400 minutos o preço por minuto é 0,15R$. Calcule sua conta de telefone.

minutos = int(input("Quantos minutos você passou no telefone? "))

if minutos < 200:
    preço = (minutos) * 0.20
    print("Seus {} minutos resultaram num total de {:.2f}R$ a ser pago.".format(minutos, preço))

if minutos > 200 and minutos <= 400:
    preço = (minutos) * 0.18
    print("Seus {} minutos resultaram num total de {:.2f}R$ a ser pago.".format(minutos, preço))

if minutos > 400:
    preço = (minutos) * 0.15
    print("Seus {} minutos resultaram num total de {:.2f}R$ a ser pago.".format(minutos, preço))