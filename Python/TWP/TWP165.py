cont = 1
soma = 0

while cont <= 10:
    num = int(input(f"Digite o {cont}º número para a soma: "))
    soma += num
    cont += 1

print(f"\nA somas de todos os números lidos é {soma}")