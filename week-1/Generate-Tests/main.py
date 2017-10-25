import math
with open('input.txt', 'r') as input:
    a = [int(x) for x in input.readline().split(' ')]

_max = 0
for n in range(2, a[0] + 1):
    _max_in = 0
    i = 2
    while i < math.sqrt(a[0]):
        if n % i == 0:
            _max_in += 1
            if not i == (n / i):
                _max_in += 1
        i += 1
    if _max_in > _max:
        _max = _max_in
with open('output.txt', 'w') as output:
    output.write(str(_max+2))
    output.write('\n')
