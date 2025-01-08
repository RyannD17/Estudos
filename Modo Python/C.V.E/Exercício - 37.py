número = int(input("Digite um número interiro: "))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
print()
opção = int(input("Sua opção: "))

if opção == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(número, bin(número)))

elif opção == 2:
    print("{} convertido para BINÁRIO é igual a {}".format(número, oct(número)))

elif opção == 3:
    print("{} convertido para BINÁRIO é igual a {}".format(número, hex(número)))

else:
    print("Opção inválida! Tente novamente")