def inserirMunicipio(nomeMunicipio, municipio):
    while True:
        try:
            nomeMunicipio = str(input("Digite um municipio: "))
            municipio.append(nomeMunicipio)
            return municipio
        except ValueError:
            print("Por favor, digite apenas nomes de municipios.")

nomeMunicipio = ""
municipio = []

inserirMunicipio(municipio)

print(municipio)