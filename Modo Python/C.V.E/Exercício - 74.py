from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f"Os valores sorteados foram: ", end="")

for n in num:
    print(f"{n}", end=" ")

print(f"\n\nO MAIOR valor sorteado foi {max(num)}.")
print(f"O MENOR valor sorteado foi {min(num)}.")

# Explicação:
# Quando trabalhamos com tuplas, ou alguns outros métodos, temos a favor a função "max" e "min".
# A grosso modo, o "max" retoma o valor MÁXIMO, ou seja, o maior valor.
# Com o "min" segue o mesmo raciocínio; ele retoma o valor MÍNIMO, ou seja, o menor valor.