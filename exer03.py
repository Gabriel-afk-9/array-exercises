va = []
vq = []
for i in range(10):
    numeros = float(input())
    va.append(numeros)

for num in va:
    quadrado = num**2
    vq.append(quadrado)

print(*va)
print(*vq)
