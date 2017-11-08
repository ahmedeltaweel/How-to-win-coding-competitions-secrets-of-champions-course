from edx_io import edx_io
import heapq

l = []
track = []
with edx_io() as io:
    n = int(io.next_int())
    for i in range(n):
        ops = io.next_token().decode('utf-8')
        if ops == '+':
            inp = int(io.next_token().decode('utf-8'))
            l.append(inp)
            track.append(inp)
            heapq.heapify(l)
        elif ops == '-':
            x = track.pop(0)
            l.remove(x)
        elif ops == '?':
            io.writeln(l[0])
