vetor_val = []

for i in range(1,6):
    valores = float(input())
    vetor_val.append(valores)
    maior = max(vetor_val)
    menor = min(vetor_val)
    media = sum(vetor_val)/len(vetor_val)

sem_col = ', '.join(map(str,vetor_val))
print(f'{sem_col}\n{maior}\n{menor}\n{media}')
