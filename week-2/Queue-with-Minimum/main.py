from edx_io import edx_io


l = []
_min = []
with edx_io() as io:
    n = int(io.next_int())
    for i in range(n):
        ops = io.next_token().decode('utf-8')
        if ops == '+':
            inp = int(io.next_token().decode('utf-8'))
            l.append(inp)
            _min.append(inp)
            _min.sort()
        elif ops == '-':
            _min.remove(l.pop(0))
        elif ops == '?':
            io.writeln(_min[0])
