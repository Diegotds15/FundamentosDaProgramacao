'''def soma(a, b):
    return a + b

def main():
    resutado = soma(3, 7)
    print(f"o resultado é {resutado}")

main()'''

'''x = 10  # Variável global

def minha_funcao():
    print(x)  # Imprime 5

minha_funcao()
print(x)  # Imprime 10'''

'''total = 0

for i in range(5):
    total += i

print(total)'''

'''preco = int(input("Qual o preço de seu produto?: "))
desconto = int(input("Qual o porcentual do desconto?: "))

valor_descontado = (preco / 100) * desconto
resultado = preco - valor_descontado
print(f"O resultado é R${resultado}")'''

'''def sub():
	global x 
	x = x - 1
	return x

x = 10

print("resultado",sub())
print(x)'''

'''def fatorial(numero):
    fat = 1
    for i in range(1, numero + 1):
        fat = fat * i
    return fat

numero = int(input("Qual o número a ser fatorado?: "))
resultado = fatorial(numero)
print(resultado)'''

'''sair = False
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
            print("A lista está vazia!")'''

def exibir_assentos(assentos):
    for i in range(15): #len(assentos)
        if assentos[i] == 0:
            print(f'Assento {i+1} esta Livre!')
        else:
            print(f'Assento {i+1} esta ocupado!')

def reservar_assento(assentos):
    num = int(input('Informe numero do assento:'))
    if num < 1 or num > 15:
        print('Assento invalido!')
    else: 
        if assentos[num-1] == 0:
            assentos[num-1] = 1
            print(f'Assento {num} reservado!')
        else:
            print('Assento esta ocupado!')

assentos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #assentos = [0] * 15
escolha ="1"

while escolha != "3":
    print('\n1. Exibir status de assento')
    print('\n2. Reservar assentos')
    print('\n3. Sair')
    print("")
    escolha = input('Informe opcao:')
    if escolha == "1":
        exibir_assentos(assentos)
    elif escolha == "2":
        reservar_assento(assentos)
    elif escolha == "3":
        print("FIM")
    else:
        print('Opcao invalida')
