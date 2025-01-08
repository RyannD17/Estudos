num = int(input(f"Digite um número para o fatorial: "))

cont = num
fat = 1

print(f"\nCalculando {num}!= ", end="")
while cont > 0:
    print(f"{cont}", end="")
    print(" x " if cont > 1 else " = ", end="")

    fat *= cont
    cont -= 1

print(f"{fat}")
print(f"\nO fatorial de {num} é {fat}.")

# Esta atividade é um questão FATORIAL. Funciona da seguinte forma:
# Digamos que eu leio o 5. O fatorial dele é 120, pois...:
# fat (5) = 5 x 4 x 3 x 2 x 1 = 120