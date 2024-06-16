# EXERCICIO 1 DE 4 CALCULO DE JUROS PELA QUANTIDADE DE PARCELA

print('Bem-vindo a loja do Evandro Nascimento')
valor_pedido = float(input('Entre com o valor do pedido: '))    # recebe o valor do pedido convertendo para float
qdt_parcelas = int(input('Entre com a quantidade de parcelas: ')) # recebe a quantidade de parcelas e convertendo para int

if qdt_parcelas < 4:    # verifica se a quantidade de parcela é menor que 4 parcelas aplica o juros que é zero por cento
    valor_parcelas = valor_pedido * (1 + 0 / 100) / qdt_parcelas
    valor_total_parcelado = valor_parcelas * qdt_parcelas
    print('O valor das parcelas é de: R$ %.2f' % valor_parcelas)
    print(f'O valor total parcelade é de: R$ {valor_total_parcelado}')

elif qdt_parcelas >= 4 and qdt_parcelas < 6:    # verifica se a quantidade de parcela é maior ou igual a 4 e menor que 6, aplica o juros de quatro por cento
    valor_parcelas = valor_pedido * (1 + 4 / 100) / qdt_parcelas
    valor_total_parcelado = valor_parcelas * qdt_parcelas
    print('O valor das parcelas é de: R$ %.2f' % valor_parcelas)
    print(f'O valor total parcelade é de: R$ {valor_total_parcelado}')

elif qdt_parcelas >= 6 and qdt_parcelas < 9:    # verifica se a quantidade de parcela é maior ou igual a 6 e menor que 9, aplica o juros de oito por cento
    valor_parcelas = valor_pedido * (1 + 8 / 100) / qdt_parcelas
    valor_total_parcelado = valor_parcelas * qdt_parcelas
    print('O valor das parcelas é de: R$ %.2f' % valor_parcelas)
    print(f'O valor total parcelade é de: R$ {valor_total_parcelado}')

elif qdt_parcelas >= 9 and qdt_parcelas < 13:   # verifica se a quantidade de parcela é maior ou igual a 9 e menor que 13, aplica o juros de dezesseis por cento
    valor_parcelas = valor_pedido * (1 + 16 / 100) / qdt_parcelas
    valor_total_parcelado = valor_parcelas * qdt_parcelas
    print('O valor das parcelas é de: R$ %.2f' % valor_parcelas)
    print(f'O valor total parcelade é de: R$ {valor_total_parcelado}')

elif qdt_parcelas >= 13:    # verifica se a quantidade de parcela é maior ou igual a 13, aplica o juros de trinta e dois por cento
    valor_parcelas = valor_pedido * (1 + 32 / 100) / qdt_parcelas
    valor_total_parcelado = valor_parcelas * qdt_parcelas
    print('O valor das parcelas é de: R$ %.2f' % valor_parcelas)
    print(f'O valor total parcelade é de: R$ {valor_total_parcelado}')

    # FIM...