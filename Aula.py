matriz =[[0, 0],
        [0, 0]]
i = 0
total_sum = 0

matriz[0][0] = int(input("Digite o valor da matriz 0, 0: "))
matriz[1][0] = int(input("Digite o valor da matriz 1, 0: "))
matriz[0][1] = int(input("Digite o valor da matriz 0, 1: "))
matriz[1][1] = int(input("Digite o valor da matriz 1, 1: "))

while i < 2:
        j = 0
        while j < 2:
                total_sum += matriz[i][j]
                j += 1
        i += 1
print("o resultado é: ", total_sum)