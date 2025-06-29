vetor_8= [1,2,3,4,5,6,7,8]
x = int(input())
y = int(input())

if 0 <= x < 8 and 0 <= y < 8:
    soma = vetor_8[x] + vetor_8[y] 
    print(soma)
else:
    print('Índices inválidos')

  