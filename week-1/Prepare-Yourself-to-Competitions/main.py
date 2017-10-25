_max = 0
p_times = None
t_times = None
with open('input.txt', 'r') as input:
    n = int(input.readline().strip().split()[0])
    t_times = input.readline().strip().split()
    p_times = input.readline().strip().split()

p_added = False
t_added = False
for i in range(n):
    if int(p_times[i]) > int(t_times[i]):
        _max += int(p_times[i])
        p_added = True
    else:
        _max += int(t_times[i])
        t_added = True

if(p_added is False):
    max_p = max(p_times)
    index = p_times.index(str(max_p))
    _max -= int(t_times[index])
    _max += int(max_p)

if(t_added is False):
    max_t = max(t_times)
    index = t_times.index(str(max_t))
    _max -= int(p_times[index])
    _max += int(max_t)

with open('output.txt', 'w') as output:
    output.write(str(_max))
    output.write('\n')
