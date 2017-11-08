o = []
with open("input.txt", 'r') as input:
    n = int(input.readline().strip())
    while n:
        l = []
        cond = True
        line = list(input.readline().strip())
        if line == '':
            o.append('YES')
            n -= 1
            continue
        for i in line:
            if i == '(' or i == '[':
                l.append(i)
                continue
            elif i == ')':
                if l and l[-1] == '(':
                    l.pop()
                else:
                    cond = False
                continue
            elif i == ']':
                if l and l[-1] == '[':
                    l.pop()
                else:
                    cond = False
                continue
        if cond and not l:
            o.append('YES')
        else:
            o.append('NO')
        n -= 1

with open('output.txt', 'w') as out:
    for i in o:
        out.write(str(i) + "\n")
