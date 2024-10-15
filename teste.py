def calculadora():
    numero1 = float(input("Digite o primeiro numero: "))
    operador = input("qual o tipo de operação (+, -, *, /): ")
    numero2 = float(input("Digite o segundo numero: "))
    

    if operador == "+":
            resultado = numero1 + numero2
    elif operador == '-':
        resultado = numero1 - numero2
    elif operador == '*':
        resultado = numero1 * numero2
    elif operador == '/':
        if numero2 == 0:
            print("Divisão por zero não é permitida!")
        else:
            resultado = numero1 / numero2
    else:
        print("Operador inválido!")

    print("Resultado:", resultado)

calculadora()