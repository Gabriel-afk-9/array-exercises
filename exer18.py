ve10 = [10,20,33,20,2,12,3,4,5,8]
mult = []

valor = int(input())

for veto in ve10:
    if veto % valor == 0:
        mult.append(veto)
print(sorted(mult))