print("{:=^40}".format(" Lojas Deyv's "))
preço = float(input("\nQual o preço da compra? R$"))
print('''\nFORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão:''')

opção = int(input("\nQual é a opção? "))

if opção == 1:
    total = preço - (preço * 10/100)

elif opção == 2:
    total = preço - (preço * 5/100)

elif opção == 3:
    total = preço
    parcela = total / 2
    print(f"\nSua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.")

elif opção == 4:
    total = preço + (preço * 20/100)
    total_pcl = int(input("\nQuantas vezes? "))
    parcela = total / total_pcl
    print(f"Sua compra será parcelada em {total_pcl}x de R${parcela:.2f} COM JUROS.")

else:
    total = preço
    print("\n\033[31mOPÇÃO INVÁLIDA! Por favor, tente novamente.")

print(f"\n\033[mSua compra de R${preço:.1f} vai custar R${total:.2f} no final.")