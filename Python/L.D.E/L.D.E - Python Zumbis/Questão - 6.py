#Questão: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:

#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

hora = float(input("Quanto você ganha por hora? R$"))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

bruto = hora * horas_trabalhadas #Calculando o Salário Bruto
Ir = bruto * (11/100) #Calculando o Imposto de Renda
Inss = bruto * (8/100) #Calculando o INSS
sindicato = bruto * (5/100) #Calculando o Sindicato

liquido = bruto - (Ir + Inss + sindicato)

print("\nDetalhamento do salário:")
print(f"+ Salário Bruto : R${bruto:.2f}")
print(f"- IR (11%) : R${Ir:.2f}")
print(f"- INSS (8%) : R${Inss:.2f}")
print(f"- Sindicato (5%) : R${sindicato:.2f}")
print(f"= Salário Líquido : R${liquido:.2f}")