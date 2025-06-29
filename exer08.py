valores = []

for i in range(1,7):
    while True:
        try:
            valor_par = int(input())
            valores.append(valor_par)
            break
        except ValueError:
            print('Numero inteiro inválido')

valores.reverse()
print(valores)