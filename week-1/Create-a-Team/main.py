
with open('input.txt', 'r') as input:
    list_1 = list(map(int, input.readline().strip().split()))
    list_2 = list(map(int, input.readline().strip().split()))
    list_3 = list(map(int, input.readline().strip().split()))

_max = 0
for i in range(3):
    f = list_1[i]
    for j in range(3):
        if j == i:
            continue
        s = list_2[j]
        for k in range(3):
            if k == j or k == i:
                continue
            t = list_3[k]
            max_1 = float((f**2 + s**2 + t**2)**.5)
            if max_1 > _max:
                _max = max_1

with open('output.txt', 'w') as output:
    output.write(str(_max))
    output.write('\n')
