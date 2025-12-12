
#Variaveis de conversão
cotacao_dolar = 5.39
cotacao_euro = 6.34
cotacao_bitcoin = 489729.00

#Print Titulo programa
print('Sistema de conversão 🪙')
while True:

    try: #Tratamento de erro.
        valor_em_real = float(input('Quanto você deseja converter?: ')) #Entrada usuário, valor em reais.
    except ValueError:
        print('Ops algo deu errado! Digite apenas números.')
        continue

    while True:

        entrada_opcoes = input("Para qual moeda deseja converter? Digite 'D' para Dólar ou 'E' para Euro ou 'B' para bitcoin: ").upper() #Entrada usuário tipo moeda.

        #Condições lógicas de conversão.
        if entrada_opcoes == 'D':
            resultado_dolar = valor_em_real / cotacao_dolar
            print(f'Seus R${valor_em_real:.2f}  reais agora são U${resultado_dolar:.2f} dolar. ')
            break

        elif entrada_opcoes == 'E':
            resultado_euro = valor_em_real / cotacao_euro
            print(f'Seus R${valor_em_real:.2f} reais agora são EUR${resultado_euro:.2f} euro. ')
            break


        elif entrada_opcoes == 'B':
            resultado_bitcoin = valor_em_real / cotacao_bitcoin
            print(f'Seus R${valor_em_real:.2f} reais agora são BTC${resultado_bitcoin:.8f} bitcoin. ')
            break
        else:
            print('Você digitou uma opção invalida, digite D / E ou B')

    #Laço de repetição caso o usuário queira fazer mais alguma conversão.
    continuar = input("Deseja fazer nova conversão? [S/N] ").upper()
    if continuar == 'N':
        print('Encerrando...')
        break

