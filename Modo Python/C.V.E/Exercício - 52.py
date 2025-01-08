num = int(input("Digite um número: "))
total = 0

for cont in range(1, num + 1): #Declarando que o "num" não vai terminar com o seu antecessor, pois a soma por 1 faz ele continuar com o valor dado.
    if num % cont == 0:
        total += 1
        print("\033[34m", end="")
    else:
        print("\033[31m", end="")

    print(f"\n{cont}", end="")

print(f"\n\n\033[mO número {num} foi dividido {total} vezes.")

if total == 2:
    print("\nPor isso ele É PRIMO!")
else:
    print("\nPor isso ele NÃO É PRIMO!")


# O "\033[34m" é um código para utilizar cores. Neste exemplo, a cor será de AZUL para os que forem divisíveis. Os que não forem deixei de vermelho "\033[31m".

# Já no "print", seguido por "\033[m", este *m* sozinho simboliza a cor comum do código printado.

# O uso do * end="" * está dizendo para o Python não adicionar nada (ou adicionar algo específico) no final do texto.
# Neste contexto, o * end="" * evita que o print pule para a próxima linha após configurar a cor, permitindo que o texto colorido apareça na mesma linha. Isso ocorre devido o uso das ASPAS VAZIAS.