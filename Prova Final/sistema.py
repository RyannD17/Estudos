print("<=>"*25)
print()
print('''Bem-vindo à loja de calçados mais famosa do Brasil, a 'KALSANDO'! 
Por favor, digite seu nome de usuário para que seu progresso seja salvo.\n''')

usuario = input("Nome de usuário: ").strip()
print()

print("<=>"*25)
print()
print(f"PERFEITO, {usuario}, agora que está logado, você pode acompanhar da melhor forma as diversas variedades de calçados da KALSANDO!\n")

# Lista de opções válidas
opcoes_validas = [1, 2]

# Função para obter uma opção válida
def obter_opcao():
    opcao = 0
    while opcao not in opcoes_validas:
        opcao = int(input('''
*Selecione uma das opções abaixo*
[ 1 ] Ir à loja
[ 2 ] Sair\n
OPÇÃO: '''))
        
        if opcao not in opcoes_validas:
            print("OPS! Parece que você digitou uma opção inválida. Por favor, tente novamente.")
    return opcao

# Chama a função para obter a opção correta
opcao_1 = obter_opcao()
print()

if opcao_1 == 1:
    print("Estes são nossos produtos:")

elif opcao_1 == 2:
    opcao_secundaria = input("Tem certeza que deseja encerrar a sessão (S/N)? ").strip().lower()

    if opcao_secundaria == "s":
        print("SESSÃO ENCERRADA!")
    elif opcao_secundaria == "n":
        print("Depois continuo kkk")