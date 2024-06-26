# SOFTWARE GERENCIAMENTO DE FUNCIONARIOS #

print("-" * 10, "Bem vindo a empresa do Evandro Nascimento", "-" * 10)
print("-" * 63)
print("-" * 24, "MENU PRINCIPAL", "-" * 23)
print("")
print("Escolha a opção desejada.")
id_global = 4154752
lista_funcionarios = []

def cadastrar_funcionario(id):
    global id_global
    global lista_funcionarios
    id_global = id
    print(f"Id do Funcionário: {id_global}")


    for i in range(1):
        nome = input("Por favor entre com o nome do Funcionário: ")
        setor = input("Por favor entre com o Setor: ")
        salario = float(input("Por favor entre com o salário do Funcionário"))
        lista_funcionarios.append([{nome, setor, salario}])

        funcionarios = [{'id': id_global,
                         'nome': nome,
                         'setor': setor,
                         'salario': salario}]

    lista_funcionarios = funcionarios.copy()




    return funcionarios


def consultar_funcionarios():

    if (opcao2 == 1):
        p = print("chamou consultar funcionarios")
        print(lista_funcionarios)

    # RETORNA A LISTA DE TODOS OS FUNCIONARIOS CADASTRADOS
    return p

while True:
    print("1 - Cadastrar Funcionários")
    print("2 - Consultar Funcionário(s)")
    print("3 - Remover Funcionário")
    print("4 - Sair")
    opcao = int(input(""))

    if (opcao == 1):
        cadastrar_funcionario(id_global)    # CHAMA A FUNÇÃO PARA CADASTRAR O FUNCIONÁRIO
        print(lista_funcionarios)
    elif (opcao == 2):
        print("-" * 63)
        print("-" * 24, "MENU CONSULTAR FUNCIONARIO", "-" * 23)
        print("")
        print("1 - Consultar Todos")
        print("2 - Consultar por ID")
        print("3 - Consultar por Setor")
        opcao2 = int(input(""))

        if (opcao2 == 1):
            consultar_funcionarios()    # CHAMA A FUNÇÃO CONSULTAR FUNCIONÁRIOS
            for funcionario in lista_funcionarios:  # FOR ITERA NA LISTA
                for chave, valor in funcionario.items():  # FOR ITERA NO DICIONÁRIO
                    print(chave, valor)

    if ( opcao == 3):
        print(opcao)
    elif ( opcao == 2):
        print(opcao)



#def lista_funcionarios ():
    #funcionario = {'Id: ':id_global,
        #'nome: ':'Evandro',
        #'setor: ':'manutenção',
        #'salario: ':1000}
    #lista = [funcionario]

    #for funcionario in lista:   # ITERA SOBRE LISTA DE FUNCIONARIOS
        #for values, keys in funcionario.items():
            #print(values, keys)
    #return lista

#consultar_funcionarios()
#consultar_funcionarios()
#print(cadastrar_funcionario(id(id_global)))