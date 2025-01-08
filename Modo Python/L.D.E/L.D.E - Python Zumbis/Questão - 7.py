#Questão: Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
# Obs. : somente são vendidos um número inteiro de latas.

area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

por_metro = 1 / 3  # 1 litro cobre 3 metros quadrados
capacidade_lata = 18  # Capacidade de cada lata em litros
preco_lata = 80.00  # Preço de cada lata

litros_necessarios = area * por_metro # Calculando da quantidade de tinta necessária

latas_necessarias = int(litros_necessarios // capacidade_lata + (litros_necessarios % capacidade_lata > 0))

custo_total = latas_necessarias * preco_lata # Calculando o custo total

print("\nInformações para pintura:")
print(f"Quantidade de latas necessárias: {latas_necessarias}")
print(f"Preço total: R$ {custo_total:.2f}")

# Explicação:
# litros_necessarios // capacidade_lata: Calcula a parte inteira da divisão.
# litros_necessarios % capacidade_lata > 0): Verifica se há resto na divisão. Se sim, adiciona 1 para garantir a próxima lata.