# SOFTWARE GERENCIAMENTO DE FUNCIONARIOS #


print("")
print("-" * 10, "Bem vindo a empresa do Evandro Nascimento", "-" * 10)
print("-" * 63)
print("-" * 24, "MENU PRINCIPAL", "-" * 23)
print("")

id_global = 4154752

while True:
    print("Escolha a opção desejada.")
    print("1 - Cadastrar Funcionários")
    print("2 - Consultar Funcionário(s)")
    print("3 - Remover Funcionário")
    print("4 - Sair")

    try:
        menu =int(input(":>> "))
    except ValueError:
        print("Opção inválida")
        continue

    if (menu == 1):
        while True:
            print(": ")
            print("-" * 63)
            print("-" * 18, "MENU CADASTRAR FUNCIONARIO", "-" * 17)
            print("-" * 63)
            print(f"Id do Funcionário: {id_global}")
            nome = input("Entre com o nome do Funcionário: ")
            setor = input("Entre com o setot do Funcionário: ")
            salario = float(input("Entre com o salário do Funcionário: "))
            if (menu == True):
                def cadastrar_funcionario ():
                    funcionarios = {'Nome: ':nome, 'Setor: ': setor, 'Salario: ':salario}
                    for i in range(1):
                        nomes = nome
                        setores = setor
                        salarios = salario
                        funcionarios.items()

                    #for x in id:
                        #id_global += 1

                    return funcionarios, nomes, setores, salarios

                print(cadastrar_funcionario())

            break
    elif (menu == 2):
        while True:
            print("1 - Consultar Todos os Funcionários")
            print("2 - Consultar Funcionário por Id")
            print("3 - Consultar Funcionário(s) por setor")
            print("4 - Retornar")
            menu2 = int(input(":>> "))
            if (menu2 == 1):
                print("consultar todos")

                def lista_funcionarios():
                    global id_global
                    funcionario = {'Id: ': id_global,
                                   'nome: ': 'Evandro',
                                   'setor: ': 'manutenção',
                                   'salario: ': 1000}
                    lista = [funcionario]
                    for funcionario in lista:  # ITERA SOBRE LISTA DE FUNCIONARIOS
                        for values, keys in funcionario.items():
                            print(values, keys)

                    return #lista
                print()
                break

            elif (menu2 == 2):
                print("consulta id")
                break
            elif (menu2 == 3):
                print("consulta setor")
                break
            elif (menu2 == 4):
                print("return")
                break
        continue
    elif (menu == 3):
        print("remover")
    elif (menu == 4):
        print("saindo")
        break
    else:
        print("Opção inválida")
        continue





