valores = []

while len(valores) < 6:
    valor_par = int(input())
    if valor_par % 2 == 0:
        valores.append(valor_par)

valores.reverse()
print(valores)