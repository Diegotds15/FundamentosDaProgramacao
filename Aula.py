perg1 = input('Está chuvendo? S - Sim/N - Não: ').upper()
perg2 = input('Tem Guarda-chuva? S - Sim/N - Não: ').upper()

if (perg1 == 'S' and perg2 == 'S') or (perg2 == 'S') or (perg1 == 'N' and perg2 == 'N'):
    print('pode sair tranquilo!')
else:
    print('não pode sair tranquilo!')