#   APP FABRICA DE CAMISETAS  DO EVANDRO NASCIMENTO  #

                # PRINT DE BOAS VINDAS #
print()
print("-" * 6, "Bem vindo a Fábrica de Camisetas do Evandro Nascimento", "-" * 6)
def escolha_modelo ():
    while True:
        print("Entre com o modelo desejado")
        print("MCS - Manga Curta Simples")
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Curta com Estampa")
        print("MLE - Manga Longa com Estampa")

        modelo = input("")
        if (modelo == "MCS"):
            valor_m = 1.80
            break
        elif (modelo == "MLS"):
            valor_m = 2.10
            break
        elif (modelo == "MCE"):
            valor_m = 2.90
            break
        elif (modelo == "MLE"):
            valor_m = 3.20
            break
        else:
            print("Escolha inválida. Entre com o modelo novamente")
            continue
    return valor_m

def num_camisetas ():
    while True:
        try:
            qtd = float(input("Entre com o número de camisetas: "))
            print()
        except ValueError:
            print("Por favor digite um valor numérico")
            continue
        if (qtd < 20):
            print("Não há desconto na venda")
            break
        elif (qtd >= 20 and qtd < 200):
            qtd -= qtd * 0.05
            break
        elif(qtd >= 200 and qtd < 2000):
            qtd -= qtd * 0.07
            break
        elif (qtd >= 2000 and qtd < 20000):
            qtd -= qtd * 0.12
            break
        else:
            print("Não aceitamos tantas camisetas de uma só vez.")
            print("Por favor, entre com o número de camisetas novamente.")
            continue
    return qtd


def frete ():
    print("Escolha um tipo de frete: ")
    print("1 - Frete por transportadora - R$ 100.00 ")
    print("2 - Frete por Sedex - R$ 200.00 ")
    print("0 - Retirar pedido na Fábrica")

    while True:
        tipo_f = int(input(""))
        if (tipo_f == 1):
            valor_f = 100
            break
        elif (tipo_f == 2):
            valor_f = 200
            break
        elif (tipo_f == 0):
            valor_f = 0
            break
        else:
            print("Digite entre as opções de 0 , 1 ou 2")
            continue
    return valor_f


total = (escolha_modelo() * num_camisetas()) + frete()

print("Total: R$ %.2f" % total)