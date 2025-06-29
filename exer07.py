vetor = []
for i in range(1,11):
    valor = int(input())
    vetor.append(valor)

maior = max(vetor)
indice = vetor.index(maior)
print(f'Vetor:{vetor}\nMaior elemento:{maior}\nPosição:{indice}')