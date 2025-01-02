cont = 0
soma = 0

while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    else:
        cont += 1
    soma += num
    
print(f"\nA média dos números lidos é {soma/cont:.1f}")

# Explicando o código:
# O "while True" quer dizer que a repetição é infinita. Ela apenas para quando digitamos 0 (condicional do código).
# Basicamente, a média será a soma dos números / quantidade de números.
# Exemplo: 30 (soma dos números) / 3 (quantidade de números) = 10.