l = {}
d = {}
d[0] = 0
l[0] = [0]
with open('input.txt', 'r') as input:
    n = int(input.readline().strip())
    for i in range(1, n + 1):
        t, m = [int(x) for x in input.readline().strip().split()]
        if m == 0:
            l[i] = l[t][:]
            x = l[i].pop()
            d[i] = d[t] - x if d[t] - x > 0 else 0
        else:
            l[i] = l[i-1] + [m]
            d[i] = d[t] + m
print(l)
print(d)
with open('output.txt', 'w') as output:
    output.write(str(sum(d.values())))
