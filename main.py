escolas = {}

def adicionar_municipio(escolas):
    municipio = input("Digite o nome do município: ")
    escolas[municipio] = {}
    print(f"Município {municipio} adicionado com sucesso!")

def adicionar_escola(escolas, municipio):
    escola = input("Digite o nome da escola: ")
    escolas[municipio][escola] = {}
    print(f"Escola {escola} adicionada ao município {municipio} com sucesso!")

def adicionar_dados_escola(escolas, municipio, escola):
    nome = input("Digite o nome da escola: ")
    endereco = input("Digite o endereço da escola: ")
    diretor = input("Digite o nome do diretor: ")
    inep = input("Digite o código INEP: ")
    escolas[municipio][escola] = {
        "nome": nome,
        "endereco": endereco,
        "diretor": diretor,
        "inep": inep
    }
    print("Dados da escola atualizados com sucesso!")

def visualizar_dados_escola(escolas):
    # Listar municípios
    print("Municípios cadastrados:")
    for municipio in escolas:
        print(municipio)

    # Escolher um município
    municipio = input("Escolha um município: ")
    if municipio in escolas:
        # Listar escolas do município
        print(f"Escolas do município {municipio}:")
        for escola in escolas[municipio]:
            print(escola)

        # Escolher uma escola
        escola = input("Escolha uma escola: ")
        if escola in escolas[municipio]:
            # Mostrar dados da escola
            dados_escola = escolas[municipio][escola]
            print(f"Dados da escola {escola}:")
            for chave, valor in dados_escola.items():
                print(f"{chave}: {valor}")
        else:
            print("Escola não encontrada.")
    else:
        print("Município não encontrado.")

while True:
    opcao = int(input("O que deseja fazer? (1 - Adicionar município, 2 - Adicionar escola, 3 - Adicionar dados da escola, 4 - Visualizar dados de uma escola, 0 - Sair): "))

    if opcao == 1:
        adicionar_municipio(escolas)
    elif opcao == 2:
        municipio = input("Digite o nome do município: ")
        if municipio in escolas:
            adicionar_escola(escolas, municipio)
        else:
            print("Município não encontrado.")
    elif opcao == 3:
        municipio = input("Digite o nome do município: ")
        if municipio in escolas:
            escola = input("Digite o nome da escola: ")
            if escola in escolas[municipio]:
                adicionar_dados_escola(escolas, municipio, escola)
            else:
                print("Escola não encontrada.")
        else:
            print("Município não encontrado.")
    elif opcao == 4:
        visualizar_dados_escola(escolas)
    elif opcao == 0:
        break
    else:
        print("Opção inválida.")