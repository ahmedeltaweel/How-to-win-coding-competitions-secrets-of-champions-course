probs = None
with open('input.txt', 'r') as input:
    n = int(input.readline().strip())
    probs = list(map(int, input.readline().strip().split(' ')))

probs.sort()
time = 300 * 60
_max = 0
for i in range(n):
    if time - probs[i] >= 0:
        time -= probs[i]
        _max += 1
    else:
        break

with open('output.txt', 'w') as output:
    output.write(str(_max))
    output.write('\n')
