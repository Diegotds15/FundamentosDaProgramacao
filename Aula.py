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

preco = int(input("Qual o preço de seu produto?: "))
desconto = int(input("Qual o porcentual do desconto?: "))

valor_descontado = (preco / 100) * desconto
resultado = preco - valor_descontado
print(f"O resultado é R${resultado}")