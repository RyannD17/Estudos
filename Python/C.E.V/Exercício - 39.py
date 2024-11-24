from datetime import date #Declarando que estamos importando a classe "date" do módulo "datetime". Essa classe é usada para trabalhar com datas
atual = date.today().year #O método "date.today()" retorna a data atual. Em seguida, usamos ".year" para extrair apenas o ano dessa data.
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento #Aqui eu criei uma variável "idade", que irá subtrair sua "idade atual" com seu ano de "nascimento"

print("\nQuem nasceu em {} tem {} anos em {}".format(nascimento, idade, atual)) #RETOMANDO O COMENTÁRIO ANTERIOR, tudo isso foi necessário para que eu desse esse "print", onde a "idade" (subtração extraída) desse o resultado exato

if idade == 18:
    print("\nVocê tem que se alistar IMEDIATAMENTE!")

elif idade < 18:
    saldo = 18 - idade #Destacando que "saldo" será os 18 anos MENOS minha "idade atual" e, consequentemente, o tempo que falta para me alistar
    ano = atual + saldo
    print("\nSeu alistamento será em {}".format(ano))
    print("Ainda faltam {} anos para o alistamento.".format(saldo))


elif idade > 18:
    saldo = idade - 18 #Destacando que "saldo" será os 18 anos MAIS minha "idade atual" e, consequentemente, o tempo que passou para me alistar
    ano = atual - saldo
    print("\nSeu alistamento foi em {}".format(ano))
    print("Você já deveria ter se alistado há {} anos.".format(saldo))