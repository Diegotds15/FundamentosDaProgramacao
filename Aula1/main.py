"""while True:
    try:
        numero1 = float(input("Digite um número: "))
        break
    except ValueError:
        print("Por favor, digite apenas números.")"""

"""variavel = 0

if(variavel == 0):
    print("Váriavel com conteúdo vazio!")
    variavel = input("Digite um valor: ")
    print(variavel)
else:
    print("Váriavel ocupada!!")

print("...Encerrando!!!...")"""
continuar_programa = True
while continuar_programa:
    print("+ = Soma")
    print("- = Subtração")
    print("* = Multiplicação")
    print("/ = Divisão")
    operador = input("Qual operação deseja fazer? Coloque seu respectivo simbolo: ")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if(operador == "+"):
        print("A soma dos números é igual a: ", numero1 + numero2)
    elif(operador == "-"):
        print("A subtração dos números é igual a: ", numero1 - numero2)
    elif(operador == "*"):
        print("A multiplicação dos números é igual a: ", numero1 * numero2)
    elif(operador == "/"):
        print("A divisão dos números é igual a: ", numero1 / numero2)
    else:
        print("Operador invalido! Tente novamente...")
    
    while True:
        resposta = input("Deseja finalizar? (s/n): ")
        if resposta.lower() == 's':
            print("Finalizando...")
            continuar_programa = False
            break
        elif resposta.lower() == 'n':
            print("Continuando...")
            break
        else:
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
