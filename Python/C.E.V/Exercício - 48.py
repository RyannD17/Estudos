soma = 0
c = 0

for cont in range (1, 501, 2):
    if cont % 3 == 0:
        c = c + 1
        soma = soma + cont

print(f"\nA somade todos os números é {soma}. Acaboou-se!")

# No "for cont in range (1, 501, 2)", o número 2 O 2 no final é o passo do loop, o que significa que ele vai pular de 2 em 2. Então ele vai pegar 1, depois 3, depois 5, e assim por diante.