#Questão: Determine se um ano é bissexto. Verifique no Google como fazer isso.

ano = int(input("Que ano quer analisar? "))
print()

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO!".format(ano))
else:
    print("O ano {} NÃO É BISSEXTO!".format(ano))