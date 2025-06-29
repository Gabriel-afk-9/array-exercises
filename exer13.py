vetores5 = []

for i in range(1,6):
    valores = int(input())
    vetores5.append(valores)
    
maior = vetores5.index(max(vetores5))
menor = vetores5.index(min(vetores5))
print(f'Posição do maior: {maior}\nPosição do menor: {menor}')
