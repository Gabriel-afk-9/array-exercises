vetor5 = []

for i in range(1,6):
    valor = float(input())
    vetor5.append(valor)

for veto in vetor5:
    valorint = int(input('Codigo:'))

    if valorint == 0:
        break
    elif valorint == 1:
        print(vetor5)
    elif valorint == 2:
        vetor5.reverse()
        print(vetor5)
    else:
        print('Código inválido')


