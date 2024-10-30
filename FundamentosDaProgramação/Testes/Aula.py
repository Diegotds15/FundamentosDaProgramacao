sair = False
quantidade = 0
nome = []

while sair != True:
    quantidade += 1
    print("")
    print("1 - Digitar um nome, Outro - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome_novo = input(f"Digite o nome {quantidade}: ")
        nome.append(nome_novo)
    else:
        sair = True

        if len(nome) > 0:
            print(f"A lista de nomes é {nome}")
        else:
            print("A lista de nomes está vazia")