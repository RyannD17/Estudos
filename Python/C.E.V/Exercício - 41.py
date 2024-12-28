from datetime import date
atual = date.today().year
nascimento = int(input("Digite seu ano de nascimento: "))
idade = atual - nascimento
print(f"\nO atleta tem {idade} anos.")

if idade <= 9:
    total = ("MIRIM")

elif idade <= 14:
    total = ("INFANTIL")

elif idade <= 19:
    total = ("JUNIOR")

elif idade <= 25:
    total = ("SÊNIOR")

else:
    total = ("MASTER")

print(f"\nClassificação: {total}")