vetores10 = [10,29,32,29,11,222,1313,9391,1,9]
repetidos = []

for vetor in vetores10:
    if vetores10.count(vetor) > 1:
        repetidos.append(vetor)

sem_col = ', '.join(map(str,repetidos))
print(sem_col)

