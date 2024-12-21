from time import sleep # O import "sleep" é usado para dar uma pausa no programa
for cont in range (10, -1, -1):
    print(cont)
    sleep(1)

print()
print("BUM! BUM! POOWW!")

# EXPLICAÇÃO

# O "sleep" está com "table", pertencendo à contagem. Caso contrário, sem esse "table" pertencente, ele iria apenas fazer a contagem para o "print('BUM! BUM! POOWW!')"

# O "for cont in range" é uma maneira de repetir um bloco de código n vezes, onde "cont" é a variável que muda a cada repetição.
# Exemplo: (10, -1, -1)
# O primeiro número (10) indica que minha repetição iniciará neste valor. 
# Já o segundo número (-1) indica que essa repetição/contagem será diminutiva, ou seja, uma contagem em que os números vão diminuindo.
# E por fim, o terceiro número (-1) indica o final desta contagem, mas há um detalhe: o final da contagem termina a um número antes ao que atribuí. Neste caso, ele finaza no 0.