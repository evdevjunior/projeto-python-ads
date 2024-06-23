#   APP DE VENDAS DE MARMITA  DE EVANDRO NASCIMENTO  #

                # PRINT DO MENU #
print()
print("-" * 6, "Bem vindo a loja de Marmitas do Evandro Nascimento", "-" * 11)
print("-" * 28, "Cardápio", "-" * 31)
print("-" * 69)
print("-" * 4, "|", " Tamanho ", "|", " Bife Acebolado(BA) ", "|", " Filé de Frango(FF) ", "|", "-" * 4)
print("-" * 4, "|", "    P    ", "|", "       R$16.00      ", "|", "      R$15.00       ", "|", "-" * 4)
print("-" * 4, "|", "    M    ", "|", "       R$18.00      ", "|", "      R$17.00       ", "|", "-" * 4)
print("-" * 4, "|", "    G    ", "|", "       R$22.00      ", "|", "      R$21.00       ", "|", "-" * 4)
print("-" * 69)

valor_total = 0 # VARIÁVEL ACUMULADORA

# LAÇO QUE REPETE A PERGUNTA DO SABOR DESEJADO
while True:
    sabor = input("Entre com o sabor desejado (BA/FF): ")   # RECEBE A ENTRADA DOS SABORES E ATRIBUI A VARIÁVEL SABOR
    if (sabor == "BA" or sabor == "FF"):  # VERIFICA SE O SABOR É DE BIFE ACEBOLADO OU FILÉ DE FRANGO BA,FF

        # LAÇO REPETE A PERGUNTA DO TAMANHO DESEJADO P,M,G
        while True:
            tamanho = input("Entre com o tamanho desejado (P/M/G): ") # RECEBE A ENTRADA DOS TAMANHOS E ATRIBUI A VARIÁVEL TAMANHO
            if (tamanho == "P" or tamanho == "M" or tamanho == "G"): # VERIFICA SE OS TAMANHOS ESTÃO CORRETOS P,M,G
                if (tamanho == "P" and sabor == "BA"): # VERIFICA O TAMANHO E SABOR
                    valor = 16.00 # RECEBE O VALOR DO SABOR PEDIDO
                    valor_total += valor # ACUMULADORA RECEBE ELA MESMA MAIS VALOR
                    print(f"Você pediu um Bife Acebolado no tamanho P: {valor}") #PRINT DO PEDIDO CONCATENADO COM A VARIÁVEL VALOR
                    break
                if (tamanho == "M" and sabor == "BA"): # VERIFICA O TAMANHO E SABOR
                    valor = 18.00
                    valor_total += valor
                    print(f"Você pediu um Bife Acebolado no tamanho M: {valor}")
                    break
                if (tamanho == "G" and sabor == "BA"): # VERIFICA O TAMANHO E SABOR
                    valor = 22.00
                    valor_total += valor
                    print(f"Você pediu um Bife Acebolado no tamanho G: {valor}")
                    break

                if (tamanho == "P" and sabor == "FF"): # VERIFICA O TAMANHO E SABOR
                    valor = 15.00
                    valor_total += valor
                    print(f"Você pediu um Filé de Frango no tamanho P: {valor}")
                    break
                if (tamanho == "M" and sabor == "FF"): # VERIFICA O TAMANHO E SABOR
                    valor = 17.00
                    valor_total += valor
                    print(f"Você pediu um Filé de Frango no tamanho M: {valor}")
                    break
                if (tamanho == "G" and sabor == "FF"): # VERIFICA O TAMANHO E SABOR
                    valor = 21.00
                    valor_total += valor
                    print(f"Você pediu um Filé de Frango no tamanho G: {valor}")
                    break
            print("Tamanho inválido. Tente novamente") # PRINT DO LAÇO CASO O TAMANHO SEJA INVÁLIDO

    else: # EXECUTA CASO O SABOR SEJA INVÁLIDO E RETORNA AO SEGUNDO LAÇO
        print("Sabor inválido. Tente novamente")
        continue
    mais = input("Deseja mais alguma coisa? (S/N):") # RECEBE O VALOR ATRIBUI A VARIÁVEL MAIS E IMPRIME A PERGUNTA ENTRE SIN OU NÃO APÓS CADA SABOR ESCOLHIDO
    if (mais == "S"): # VERIFICA SE O CLIENTE QUER COMPRAR MAIS E RETORNA AO PRIMEIRO LAÇO
        continue
    print(f"O Valor total a ser pago R$ {valor_total}") # IMPRIME O TOTAL DOS PEDIDOS
    break # PARA O PROGRAMA FINALIZANDO O PRIMEIRO LAÇO