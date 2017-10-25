with open('input.txt', 'r') as input:
    a0, a1, a2, n = [int(x) for x in input.readline().split(' ')]

x = [a0, a1, a2]
i = 3
for z in range(n - 2):
    x.append(x[i - 1] + x[i - 2] - x[i - 3])
    i += 1
with open('output.txt', 'w') as output:
    output.write(str(x.pop()))
    output.write('\n')
