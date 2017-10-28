f = open('input.txt', 'r')
k = int(f.readline().strip())
f.close()

dc = 1
hcn = 1

for a in range(0, 10):  # 2
    for b in range(0, 10):  # 3
        for c in range(0, 6):  # 5
            for d in range(0, 4):  # 7
                for e in range(0, 3):  # 11
                    for f in range(0, 3):  # 13
                        for g in range(0, 2):  # 17
                            number = (2 ** a) * (3 ** b) * (5 ** c) * \
                                    (7 ** d) * (11 ** e) * \
                                    (13 ** f) * (17 ** g)
                            if number <= k:
                                divisors = (a + 1) * (b + 1) * (c + 1) * \
                                        (d + 1) * (e + 1) * (f + 1) * (g + 1)
                                if dc < divisors:
                                    dc = divisors
                                    hcn = number
                                elif dc == divisors and number < hcn:
                                    hcn = number

f = open('output.txt', 'w')
f.write(str(k - hcn + 1) + '\n')
f.close()
