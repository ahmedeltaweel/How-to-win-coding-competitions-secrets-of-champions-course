with open('input.txt', 'r') as input:
    a0, a1, a2, n = [int(x) for x in input.readline().split(' ')]

with open('output.txt', 'w') as output:
    output.write(str(x.pop()))
    output.write('\n')
