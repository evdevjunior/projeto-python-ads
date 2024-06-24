# SOFTWARE GERENCIAMENTO DE FUNCIONARIOS #

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
    opcao = int(input(""))

    if ( opcao == 1):
        def cadastrar_funcionario(id):
            global id_global
            id_global = id
            nome = input("Por favor entre com o nome do Funcionário: ")
            setor = input("Por favor entre com o Setor: ")
            salario = float(input("Por favor entre com o salário do Funcionário"))
            funcionarios = [id_global, nome, setor, salario]
            list_funcionario = funcionarios.copy()

            return list_funcionario
        break

    elif ( opcao == 2):
        def consultar_funcionarios():
            print("-" * 63)
            print("-" * 24, "MENU CONSULTAR FUNCIONARIO", "-" * 23)
            print("")
            print("1 - Consultar Todos")
            print("2 - Consultar por ID")
            print("3 - Consultar por Setor")
            opcao2 = int(input(""))
            if ( opcao2 == 1):
                print("")
                lista_funcionarios()  # RETORNA A LISTA DE TODOS OS FUNCIONARIOS CADASTRADOS
            return opcao2
        break
    continue

def lista_funcionarios ():
    funcionario = {'Id: ':id_global,
        'nome: ':'Evandro',
        'setor: ':'manutenção',
        'salario: ':1000}
    lista = [funcionario]

    for funcionario in lista:   # ITERA SOBRE LISTA DE FUNCIONARIOS
        for values, keys in funcionario.items():
            print(values, keys)
    return lista

#consultar_funcionarios()
#consultar_funcionarios()
print(cadastrar_funcionario(id(id_global)), consultar_funcionarios())