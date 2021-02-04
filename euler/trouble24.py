result = ""
count= 0

def number(count):
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    for e in range(0, 10):
                        for f in range(0, 10):
                            for g in range(0, 10):
                                for h in range(0, 10):
                                    for i in range(0, 10):
                                        for j in range(0, 10):
                                            if a == b or a == c or a == d or a == e or a == f or a == g or a == h or a == i or a == j or b == c or b == d or b == e or b == f or b == g or b == h or b == i or b == j or c == d or c == e or c == f or c == g or c == h or c == i or c == j or d == e or d == f or d == g or d == h or d == i or d == j or e == f or e == g or e == h or e == i or e == j or f == g or f == h or f == i or f == j or g == h or g == i or g == j or h == i or h == j or i == j:
                                                continue
                                            else:
                                                result = str(
                                                    a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j)
                                                count += 1
                                                print(result)
                                            if count == 1000000:
                                                return print(result)

print(number(0))
