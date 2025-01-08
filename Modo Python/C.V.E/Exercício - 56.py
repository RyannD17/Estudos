soma_idade = 0
média_idade = 0
maior_idade_homem = 0
nome_velho = ""
total_mulher_20 = 0

for pessoa in range(1, 5):
    print(f"\n----- {pessoa}ª pessoa -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))

    soma_idade = soma_idade + idade

    if pessoa == 1 and sexo in "Mn": #| Declarando que a 1ª pessoa HOMEM
        maior_idade_homem = idade    #| ao digitar seu nome, idade e sexo
        nome_velho = nome            #| ocupará o MAIOR e o MENOR valor atribuído a estas variáveis.

    if sexo in "Mn" and idade > maior_idade_homem: # Se o HOMEM digitar seu sexo com a letra "M" ou "m" será válido.
        maior_idade_homem = idade # Se a idade dele for MAIOR que a idade da 1ª pessoa HOMEM, então a maioridade
        nome_velho = nome # será atribuído a ele. Logo, teremos controle do homem mais velho.

    if sexo in "Ff" and idade < 20: # Próximo ao 2º comentário, se a MULHER digitar seu sexo com a letra "F" ou "f" será válido.
        total_mulher_20 += 1 # Declarando a contagem das mulheres menores que 20 anos pela soma (+ 1).

    
média_idade = soma_idade / 4
print(f"\nA média das idades é {média_idade}.")
print(f"\nO homem mais velho tem {maior_idade_homem} anos, e se chama {nome_velho}.")
print(f"Ao todo são {total_mulher_20} mulheres com menos de 20 anos.")