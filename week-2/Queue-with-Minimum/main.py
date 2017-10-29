from edx_io import edx_io
from collections import deque
l = deque()
_min = 1000000000
with edx_io() as io:
    n = int(io.next_int())
    for i in range(n):
        ops = io.next_token()
        if ops.decode('utf-8') == '+':
            inp = io.next_token().decode('utf-8')
            if int(inp) < _min:
                _min = int(inp)
            l.append(inp)
        elif ops.decode('utf-8') == '-':
            l.popleft()
            _min = 1000000000
            for i in l:
                if int(i) < _min:
                    _min = int(i)
        elif ops.decode('utf-8') == '?':
            io.writeln(_min)
