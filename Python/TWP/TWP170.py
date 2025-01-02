cont = 1
fat = 1

num = int(input(f"Digite um número para a multiplicação: "))
while cont <= num:
    fat *= cont
    cont += 1

print(f"\nO fatorial de {num} é {fat}")

# Esta atividade é um questão FATORIAL. Funciona da seguinte forma:
# Digamos que eu leio o 5. O fatorial dele é 120, pois...:
# fat (5) = 5 x 4 x 3 x 2 x 1 = 120