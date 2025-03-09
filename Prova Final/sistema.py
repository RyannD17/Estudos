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
opcoes_validas = [1, 2, 3]

# Função para obter uma opção válida
def obter_opcao():
    opcao = 0
    while opcao not in opcoes_validas:
        opcao = int(input('''
*Selecione uma das opções abaixo*
[ 1 ] Ir à loja
[ 2 ] Sobre a KALSANDO
[ 3 ] Sair\n
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
    print('''SOBRE A KALSANDO\n\n A KALSANDO é uma das melhores lojas de calçados do Brasil, na qual bateu record no total de calçados vendidos somente no ano de 2017, levando o país a patamares históricos em toda America Latina.\n Fundado pelo diretor Ryann Deyv's, a KALSANDO surgiu através de uma dependência na matéria escolar do seu curso de informática Para Internet, onde ele desenvolveu um sistema simples de interação com o usuário acerca dos calçados brasileiros. Com isso, as amostras coletadas desse sistema serviu como base para erguer a famosa KALSANDO, na qual R. Deyv's adiministra este site juntamente com sua equipe especializada no ambiente virtual.\n Assim, transformamos a loja, tanto física quanto online, num ambiente profissional e criativo com a sua maior prioridade, QUE É VOCÊ CLIENTE.''')

elif opcao_1 == 3:
    opcao_secundaria = input("Tem certeza que deseja encerrar a sessão (S/N)? ").strip().lower()

    if opcao_secundaria == "s":
        print("SESSÃO ENCERRADA!")
    elif opcao_secundaria == "n":
        print("Depois continuo kkk")