vetor_10 = [10,20,23,42,42,33,112,32,-2,-3]

for vetor in range(len(vetor_10)):
    if vetor_10[vetor] < 0:
        vetor_10[vetor] = 0

print(vetor_10)