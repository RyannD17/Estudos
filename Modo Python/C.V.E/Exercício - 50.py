soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f"Digite o {c} valor: "))
    if num % 2 == 0:
        soma += num
        cont += 1

print()
print(f"Você digitou {cont} números PARES, e a soma foi {soma}.")

# O motivo de iniciarmos a SOMA e a CONTAGEM (CONT) com 0 se dá porque nenhuma SOMA ou CONT foi iniciada.

# Já na condicional, a "SOMA += num" = "SOMA = SOMA + num". Isso quer dizer que se eu adicionar 2, 4 e 6 -- por exemplo -- ele vai somar:
# SOMA = 0 (valor dado inicialmente) + 2 (1º número digitado) = 2; DEPOIS: 2 (resultado da primeira operação) + 4 (2º número digitado) = 6; e assim por diante.

# Continuando na condicional, temos a variável CONT, que é usada para contar quantos números PARES foram digitados. No exemplo da SOMA será exibido 3, pois é o total de números PARES dados pelo.