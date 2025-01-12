listagem = ("Lápis", 245,
            "Borracha", 120.75,
            "Caderno", 207.85,
            "Estojo", 669.99,
            "Mochila", 1.450)

print("-" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}") # O símbolo "^" indica um espaçamento alinhado ao texto. O número ao lado define o quanto.
print("-" * 40)

for pos in range(0, len(listagem)): # Percorre desde o início até o último índice da lista.
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="") # O símbolo "<" indica um espaçamento à esquerda.
    else:
        print(f"{listagem[pos]:>7.2f}") # O símbolo "<" indica um espaçamento à direita.
print("-" * 40)