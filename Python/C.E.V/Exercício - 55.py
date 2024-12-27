maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input(f"Qual o peso da {pessoa}ª pessoa? "))

    if pessoa == 1:  #| Declarando que a 1ª pessoa
        maior = peso #| ao digitar seu peso ocupará
        menor = peso #| o MAIOR e o MENOR peso.
    else:
        if peso > maior: #| A 1ª pessoa que digita o peso será tanto maior quanto menor, pois só tem a dela.
            maior = peso #| Mas, se digitar um peso maior, então MAIOR será o novo peso seguinte, mostrado no código
        if peso < menor: #| E se ao digitar um peso menor, então MENOR será o novo peso seguinte, mostrado mo código
            menor = peso #| Assim, teremos um controle do peso MAIOR e MENOR digitados.

print(f"\nO maior peso lido foi {maior}Kg. E o menor peso foi {menor}Kg")