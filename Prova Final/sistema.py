print("<=>"*25)
print()
print('''Bem-vindo à loja de calçados mais famosa do Brasil, a 'KALSANDO'! 
Por favor, digite seu nome de usuário para que seu progresso seja salvo.\n''')

usuario = input("Nome de usuário: ").strip()
print()
print("<=>"*25)
print()
print(f"PERFEITO, {usuario}, agora que está logado, acompanhe as variedades de calçados da KALSANDO!")

# Dicionário de produtos com preços
produtos = {
    "Tênis Mike": 349.90,
    "Tênis Ardidas": 359.90,
    "Sandália Havanas": 49.90,
    "Sapato Social": 199.90
}

# Carrinho de compras (lista de produtos adicionados)
carrinho = []

# Função para mostrar o menu principal
def menu_principal():
    while True:
        try:
            print("\n*** MENU PRINCIPAL ***")
            print("[ 1 ] Ir à loja")
            print("[ 2 ] Sobre a KALSANDO")
            print("[ 3 ] Ver Carrinho")
            print("[ 4 ] Finalizar Compra")
            print("[ 5 ] Sair")
            
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 1:
                loja()
            elif opcao == 2:
                sobre()
            elif opcao == 3:
                ver_carrinho()
            elif opcao == 4:
                finalizar_compra()
            elif opcao == 5:
                sair()
                break
            else:
                print("OPS! Opção inválida. Por favor, tente novamente.")
        except ValueError:
            print("ERRO: Digite apenas números inteiros.")

# Função da loja para exibir e adicionar produtos
def loja():
    while True:
        print("<=>"*25)
        print("\n*** LOJA DE CALÇADOS ***")
        print("Veja nossos produtos disponíveis:")
        for idx, (produto, preco) in enumerate(produtos.items(), 1):
            print(f"[ {idx} ] {produto} - R$ {preco:.2f}")
        print("[ 0 ] Voltar ao menu")
        
        try:
            escolha = int(input("\nDigite o número do produto que deseja adicionar ao carrinho: "))
            if escolha == 0:
                break
            elif 1 <= escolha <= len(produtos):
                produto_escolhido = list(produtos.keys())[escolha - 1]
                carrinho.append(produto_escolhido)
                print(f"Produto '{produto_escolhido}' adicionado ao carrinho!")
            else:
                print("Produto inexistente. Tente novamente.")
        except ValueError:
            print("ERRO: Digite apenas números inteiros.")

# Função sobre a KALSANDO
def sobre():
    print('''\n*** SOBRE A KALSANDO ***\n\nA KALSANDO é uma das melhores lojas de calçados do Brasil, recordista de vendas desde 2017, levando o país a patamares históricos em toda America Latina! Fundada por Ryann Deyv's, ela surgiu através de um projeto do curso de Informática Para Internet, onde se transformou em sucesso nacional. Atualmente, R. Deyv's administra este site juntamente com sua equipe especializada no ambiente virtual. Hoje, somos referência em moda e conforto para seus pés, levando o bem-estar para nossa maior prioridade, QUE É VOCÊ CLIENTE!''')
    print("<=>"*25)

# Função para ver o carrinho e gerenciar
def ver_carrinho():
    while True:
        print("\n*** SEU CARRINHO ***")
        if not carrinho:
            print("Seu carrinho está vazio.")
            break
        else:
            total = 0
            for idx, item in enumerate(carrinho, 1):
                preco = produtos[item]
                total += preco
                print(f"[ {idx} ] {item} - R$ {preco:.2f}")
            print(f"\nTOTAL ATUAL DO CARRINHO: R$ {total:.2f}")
            
            print("\n[ 1 ] Remover Produto")
            print("[ 2 ] Continuar Comprando")
            print("[ 0 ] Voltar ao Menu Principal")
            try:
                escolha = int(input("Escolha uma opção: "))
                if escolha == 1:
                    idx_remover = int(input("Digite o número do produto para remover: "))
                    if 1 <= idx_remover <= len(carrinho):
                        removido = carrinho.pop(idx_remover - 1)
                        print(f"Produto '{removido}' removido com sucesso!")
                    else:
                        print("Produto não encontrado no carrinho.")
                elif escolha == 2:
                    loja()
                    break
                elif escolha == 0:
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("ERRO: Digite apenas números inteiros.")

# Função para finalizar compra e mostrar total final
def finalizar_compra():
    if not carrinho:
        print("\nSeu carrinho está vazio! Adicione produtos antes de finalizar a compra.")
        return
    
    print("\n*** FINALIZAR COMPRA ***")
    total = 0
    for idx, item in enumerate(carrinho, 1):
        preco = produtos[item]
        total += preco
        print(f"[ {idx} ] {item} - R$ {preco:.2f}")
    print(f"\nTOTAL A PAGAR: R$ {total:.2f}")
    
    while True:
        confirmar = input("\nDeseja concluir a compra? (S/N): ").strip().lower()
        if confirmar == "s":
            print(f"\nCompra finalizada com sucesso! Obrigado por comprar na KALSANDO, {usuario}!")
            print("<=>"*25)
            carrinho.clear()  # esvaziar carrinho
            break
        elif confirmar == "n":
            print("Compra não finalizada. Você pode continuar navegando.")
            break
        else:
            print("Opção inválida. Digite 'S' para sim ou 'N' para não.")

# Função para encerrar o sistema
def sair():
    while True:
        confirma = input("\nTem certeza que deseja sair? (S/N): ").strip().lower()
        if confirma == "s":
            print(f"\nSESSÃO ENCERRADA. Obrigado por visitar a KALSANDO, {usuario}!")
            print("<=>"*25)
            break
        elif confirma == "n":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Digite 'S' para sim ou 'N' para não.")

# Iniciar o menu principal
menu_principal()
