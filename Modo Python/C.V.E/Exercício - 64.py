num = cont = soma = 0
num = int(input("Digite um número [999 para parar]: "))

while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número [999 para parar]: "))

print(f"\nVocê digitou {cont} números e a soma entre eles {soma}")

# Explicação:
# num: Armazena o número digitado pelo usuário.
# cont: Conta quantos números foram digitados (exceto o valor sentinela 999).
# soma: Acumula a soma de todos os números digitados.