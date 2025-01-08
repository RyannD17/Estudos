from datetime import date
atual = date.today().year

total_maior = 0
total_menor = 0

for pessoa in range(1, 8):
    nascimento = int(input(f"Em que ano a {pessoa}ª pessoa nasceu? "))

    idade = atual - nascimento

    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1

print(f"\nAo todo, tivemos {total_maior} pessoas de maior e {total_menor} de menor.")


# from datetime import date | Declarando a data atual
# atual = date.today().year | para poder fazer o código

# Os "total_m..." são para iniciar uma contagem de quantos são de maior ou de menor.
# Exemplo: 1970 (0 + 1) = 1ª pessoa de maior.
# 0 é o total do "total_maior" inicial + 1 que adicionamos na condicional. Assim também ocorre para o "total_menor".