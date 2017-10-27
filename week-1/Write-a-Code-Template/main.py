keyboard = []
w, h = 0, 0
counts = []
langs = []


def get_max_time(c1, c2):
    x = [x for x in keyboard if c1 in x][0]
    c1_x, c1_y = keyboard.index(x), x.index(c1)
    x = [x for x in keyboard if c2 in x][0]
    c2_x, c2_y = keyboard.index(x), x.index(c2)
    c_x_diff = c1_x - c2_x
    c_y_diff = c1_y - c2_y
    return max(abs(c_x_diff), abs(c_y_diff))


with open('input.txt', 'r') as input:
    w, h = [int(x) for x in input.readline().split(' ')]
    for i in range(h):
        keyboard.append(list(input.readline().strip()))
    for i in range(3):
        langs.append(input.readline().strip())
        # skip template start
        skipp = input.readline().strip()
        cnt = 0
        line = ''
        while(1):
            _line = input.readline().strip()
            if _line == '%TEMPLATE-END%':
                break
            line += _line
            line = ''.join(line.split(' '))
        for j in range(len(line) - 1):
            cnt += get_max_time(line[j], line[j + 1])
        counts.append(cnt)

_min = min(counts)
index = counts.index(_min)
with open('output.txt', 'w') as output:
    output.write(str(langs[index]))
    output.write('\n')
    output.write(str(counts[index]))
