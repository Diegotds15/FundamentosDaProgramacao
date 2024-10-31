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
            print("A lista está vazia!")
