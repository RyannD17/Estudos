from time import sleep

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

opção = 0

while opção != 5:
    print('''\n    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números 
    [ 5 ] sair do programa''')

    opção = int(input("\n>>>>>> Qual vai ser a opção? "))

    if opção == 1:
        soma = n1 + n2
        print(f"\nA soma entre {n1} e {n2} é {soma}.")

    elif opção == 2:
        mult = n1 * n2
        print(f"\nA resultado entre {n1} x {n2} é {mult}.")

    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"\nEntre {n1} e {n2} o maior valor é {maior}.")

    elif opção == 4:
        print("Informe os novos números:")
        n1 = int(input("\nPrimeiro valor: "))
        n2 = int(input("Segundo valor: "))

    elif opção == 5:
        print("Finalizando...")

    else:
        print("Opção inválida. Tente novamente.")
    print("=-=" * 20)
    sleep(3)

print("\nFim do programa! Volte sempre!")