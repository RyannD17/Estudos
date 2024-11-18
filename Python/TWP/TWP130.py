#Questão: Retomando o que fizemos na questão "TWP125"... Modifique o programa da empresa Tchau para uma promoção onde a tarifa é de 0,08R$ quando você utiliza mais que 800 minutos.

minutos = int(input("Quantos minutos você passou no telefone? "))

#Retomando o que fizemos na questão "TWP125", porém, utilizando o ELIF

if minutos < 200:
    preço = (minutos) * 0.20
    print("Seus {} minutos resultaram num total de {:.2f}R$ a ser pago.".format(minutos, preço))

elif minutos <= 400:
    preço = (minutos) * 0.18
    print("Seus {} minutos resultaram num total de {:.2f}R$ a ser pago.".format(minutos, preço)) #O uso do ELIF quer dizer algo como "Se NÃO for verdade...", diferente do ELSE que apenas introduz "Se NENHUMA das condições for verdadeira..."

elif minutos <= 800:
    preço = (minutos) * 0.15
    print("Seus {} minutos resultaram num total de {:.2f}R$ a ser pago.".format(minutos, preço))

elif minutos > 800:
    preço = (minutos) * 0.08
    print("Seus {} minutos resultaram num total de {:.2f}R$ a ser pago.".format(minutos, preço))