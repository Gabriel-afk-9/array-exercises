provas = []

for i in range(1,16):
    while True:
        try:
            notas = float(input())
            if 0 <= notas <= 10:
                provas.append(notas)
                break
        except ValueError:
            print('Valor inválido')

media = sum(provas)/len(provas)
media_arredondada = round(media,2)
print(f'Média geral: {media_arredondada}')