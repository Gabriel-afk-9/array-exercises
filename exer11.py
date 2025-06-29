vetor_real = []

for i in range(1,11):
    numeros = float(input())
    vetor_real.append(numeros)

cont = 0
soma = 0
for num in vetor_real:
    if num < 0:
        cont += 1
    elif num > 0:
        soma += num

print(f'Quantitade de negativos: {cont}\nSoma dos positivos: {soma}')
