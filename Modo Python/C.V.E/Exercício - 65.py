resp = "S"
soma = quant = média = maior = menor = 0

while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    print()
média = soma / quant

print(f"Você digitou {quant} números e a média foi {média}.")
print(f"O maior e menor valor foram, respectivamente, {maior} e {menor}.")

# Explicação:
# Começando com o "S" (SIM) para não haver necessidade de perguntar ao usuário se ele deseja continuar logo no início.
# Já que o programa precisa de pelo menos uma iteração antes de perguntar.