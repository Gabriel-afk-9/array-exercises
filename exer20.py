vetor10 = []
impares = []

i = 0
while i < 10:
    for i in range(10):
        num = int(input())
        if 0 <= num <= 50:
            vetor10.append(num)
            i += 1

for im in vetor10:
    if im % 2 != 0:
        impares.append(im)

def mostrar(vetor):
    for u in range(0,len(vetor),2):
        print(*vetor[u:u+2])

mostrar(vetor10)
mostrar(impares)

