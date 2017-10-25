with open('input.txt', 'r') as input:
    a0, a1, a2 = [float(x) for x in input.readline().split(' ')]

res = float((a0 / 2 + a1 / 2 + a2 / 2)/3)
with open('output.txt', 'w') as output:
    output.write(str(float(res)))
    output.write('\n')
