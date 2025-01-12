cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
        "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    print("Tente novamente. ", end="")

print(f"\nVocê digitou o número {cont[num]}.")

# Explicação:
# O "{cont[num]}" usa o valor de "num" para acessar o correspondente textual da tupla cont.