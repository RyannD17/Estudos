peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    total = "ABAIXO DO PESO!"

elif 18.5 <= imc < 25:
    total = "no PESO IDEAL!"

elif 25 <= imc < 30:
    total = "em SOBREPESO!"

elif 30 <= imc < 40:
    total = "em OBESIDADE!"

else:
    total = "em OBESIDADE MÓRBIDA! PROCURE UM MÉDICO!"

print(f"\nO seu IMC é de {imc:.1f}. Logo, você está {total}")