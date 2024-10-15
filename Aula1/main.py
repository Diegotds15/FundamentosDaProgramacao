while True:
    try:
        numero1 = float(input("Digite um número: "))
        break
    except ValueError:
        print("Por favor, digite apenas números.")