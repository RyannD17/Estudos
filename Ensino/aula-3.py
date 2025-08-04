while True:
    try:
        numero = float(input("Digite um número: "))
        print("Você digitou:", numero)
        break  # Sai do loop se der tudo certo
    except ValueError:
        print("Erro: Por favor, digite um número válido.")