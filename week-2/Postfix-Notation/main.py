with open('input.txt', 'r') as input:
    n = int(input.readline().strip())
    ops = input.readline().strip().split(' ')

l = []
for i in ops:
    if i == '+':
        x = int(l.pop())
        y = int(l.pop())
        l.append((x + y))
    elif i == '-':
        x = int(l.pop())
        y = int(l.pop())
        l.append((y - x))
    elif i == '*':
        x = int(l.pop())
        y = int(l.pop())
        l.append((x * y))
    else:
        l.append(i)

with open('output.txt', 'w') as output:
    output.write(str(l.pop()))
